
import sys
# globals
if sys.argv[1] == None: 
	pdffile = 'book1.pdf'
else:
	pdffile = sys.argv[1]

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open(pdffile, "rb"))

# print how many pages input1 has:
print ("pdf has %d pages." % input1.getNumPages())
print (input1.getDocumentInfo())
print (input1.getXmpMetadata())
if input1.isEncrypted:
	print('encrypted')
else:
	print('not encrypted')
i = 4
content = ""
while i < 6:
	texter = input1.getPage(i).extractText()
	#print(texter)
	i = i + 1
	content +=  texter + "\n"
	content = " ".join(content.replace("\xa0", " ").strip().split())
#content.encode("ascii", "ignore")
#print(content.encode("ascii", "ignore"))
# add page 1 from input1 to output document, unchanged
output.addPage(input1.getPage(0))

# add page 2 from input1, but rotated clockwise 90 degrees
output.addPage(input1.getPage(1).rotateClockwise(90))

# add page 3 from input1, rotated the other way:
output.addPage(input1.getPage(2).rotateCounterClockwise(90))
# alt: output.addPage(input1.getPage(2).rotateClockwise(270))

# add page 4 from input1, but first add a watermark from another PDF:
page4 = input1.getPage(3)
watermark = PdfFileReader(open(pdffile, "rb"))
page4.mergePage(watermark.getPage(0))
output.addPage(page4)


# add page 5 from input1, but crop it to half size:
page5 = input1.getPage(4)
page5.mediaBox.upperRight = (
    page5.mediaBox.getUpperRight_x() / 2,
    page5.mediaBox.getUpperRight_y() / 2
)
output.addPage(page5)

# add some Javascript to launch the print window on opening this PDF.
# the password dialog may prevent the print dialog from being shown,
# comment the the encription lines, if that's the case, to try this out
output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

# encrypt your new PDF and add a password
#password = "secret"
#output.encrypt(password)

# finally, write "output" to document-output.pdf
outputStream = open("PyPDF2-output.pdf", "wb")
output.write(outputStream)



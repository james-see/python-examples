
#!/usr/bin/python3
# Author: James Campbell
# Date: 03-15-2017
# What: take a pdf and get text from it using pdfquery
import sys
import pdfquery
import random
import pickle

# globals
if sys.argv[1] == None: 
	pdffile = 'book1.pdf'
else:
	pdffile = sys.argv[1]

pdf = pdfquery.PDFQuery(pdffile)
pdf.load()
text = pdf.pq.text()
#with open('discordia.pkl', 'wb') as f:
#	pickle.dump(text, f)
#exit()
def getran(tex):
	texter = random.choice(tex)
	if len(texter) < 140 and len(texter) > 0:
		return texter
	else:
		global text
		globular = getran(text)
	return globular
#print(getran(text))
if text != '':
	print(text)
else:
	exit('need to ocr pdf first')

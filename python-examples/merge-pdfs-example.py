#!/usr/bin/python3
# Author: James Campbell
# Date: 2017-03-07
# Date Updated: 2019-06-19
# What: combine a list of pdfs into one pdf from assets/testpdf1.pdf & testpdf2.pdf
from PyPDF2 import PdfFileMerger, PdfFileReader

filenames = ["assets/testpdf1.pdf", "assets/testpdf2.pdf"]
merger = PdfFileMerger()
for filename in filenames:
    merger.append(PdfFileReader(open(filename, "rb")))
merger.write("./assets/pypdf2_example_output.pdf")

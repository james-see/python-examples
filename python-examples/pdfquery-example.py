#!/usr/bin/python3
# Author: James Campbell
# Date: 03-15-2017
# Last Modified 06-03-2019
# What: take a pdf and get text from it using pdfquery
import sys
import pdfquery

# globals
if sys.argv[1] == None:
    pdffile = "book1.pdf"
else:
    pdffile = sys.argv[1]

pdf = pdfquery.PDFQuery(pdffile)
pdf.load()
text = pdf.pq.text()
if text != "":
    print(text)
else:
    exit("need to ocr pdf first")

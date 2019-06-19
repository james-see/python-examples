#!/usr/bin/python3
# Author: James Campbell
# Date: June 3rd 2019
# What: get text from a PDF
import sys
import textract

text = textract.process(f"{sys.argv[1]}")
print(text)

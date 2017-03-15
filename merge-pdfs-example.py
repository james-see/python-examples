#!/usr/bin/python3
# Author: James Campbell
# Date: March 15th 2017
# What: combine a list of pdfs into one pdf
import glob
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
from configs import * # set a configs.py file with fullpath var
# can pass in prefix for files in filenames
prefix = 'page_'
if len(sys.argv) > 1:
	print(sys.argv[1])
	if sys.argv[1] in ['help','--help','-h']:
		print('arguments: \nyou can pass --pre or -p and the prefix of your pdf files to combine\n-o for output file (must pass -p and -o) otherwise default merged.pdf-h or --help for this help menu')
	if sys.argv[1] in ['-o','-O','--output']:
		outputfilename = sys.argv[2]
	else:
		outputfilename = 'merged.pdf'
	if sys.argv[1] in ['-pre','--pre','-p']:
		prefix = sys.argv[2]
	else:
		prefix = 'page_'
	if len(sys.argv) > 3:
		if sys.argv[3] in ['--output','-o','-O']:
			outputfilename = sys.argv[4]
		else:
			outputfilename = 'merged.pdf'
filenames = glob.glob(fullpath+prefix+"*.pdf")
merger = PdfFileMerger()
for filename in filenames:
    merger.append(PdfFileReader(open(filename, 'rb')))
merger.write(outputfilename)
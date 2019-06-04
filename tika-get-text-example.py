#!/usr/bin/python3
# Author: James Campbell
# Date: June 3rd 2019
# What: get text from a PDF
from tika import parser
import sys
text = parser.from_file(f"{sys.argv[1]}")
print(text)
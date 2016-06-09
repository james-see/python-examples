#!/usr/bin/python
# Author: James Campbell
# Date: June 9th 2016
# Date Updated:
# What: Example of how to use argparse moduel properly (Python3)

import argparse, sys
parser = argparse.ArgumentParser(description='Example on how to use argparse',
                                 prog="argparse example",
                                 )

parser.add_argument('-a', action="store_false", default=None,
                    help='Turn A off',
                    )
parser.add_argument('+a', action="store_true", default=None,
                    help='Turn A on',
                    )
parser.add_argument('-v','--version', action='version', version='VERSION 2.0',)
parser.add_argument('--verbose',
    action='store_true',
    help='verbose flag' )
args = parser.parse_args()
if args.verbose:
    print("~ Very Verbose!")
else:
    print("~ Not verbose")

sys.exit()

# pattern library example querying Google using the context and terms option to get weights and comparisons
# author: James Campbell
# Date Created: 2015 05 18
# to install pattern, it is simple via pip: pip install pattern

import sys # need this to pass arguments at the command line
from termcolor import colored # awesome color library for printing colored text in the terminal
import argparse
import random

# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store', dest='simple_value',
                    help='Search term')
parser.add_argument('-c', action='store', dest='context',
                    help='Set the context term to search on in Google')
parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')
parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )
parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.1')
results = parser.parse_args()

# check to see if the context term is set at the command line, otherwise set it to dangerous as default
if results.context != None:
     contexter = results.context
else: contexter = 'dangerous'

# global dictionary list of terms - do not change
diction = []
subset = []
lengthmin = 6
numterms = 10
fname = '/Users/mbpjc/projects/python-examples/assets/dictionary-list.html'
with open(fname) as f:
    diction = f.readlines()
    for term in diction:
     if len(term) > lengthmin:
          subset.append(term)

# function to get a random term from the minlength dictionary in subset list
def rando(listofterms,num):
     i = 0
     while i < num:
          randomed = random.choice(listofterms)
          #print randomed
          searchlist.append(randomed)
          i = i + 1
     return

searchlist = [] # the list of terms that will be generated in the rando function
# setup the default search terms 
rando(subset,numterms) # get total list of terms based on numterms set in the globals section above
from pattern.web import sort
 
results = sort(terms=searchlist,context=contexter,prefix=True)
for weight, term in results:
     print "%.2f" % (weight * 100) + '%', term
exit()

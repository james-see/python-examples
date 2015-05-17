# pattern library examples including querying Twitter, Google, and others
# author: James Campbell
# Date Created: 2015 05 17
# to install pattern, it is simple via pip: pip install pattern

import sys # need this to pass arguments at the command line
from termcolor import colored # awesome color library for printing colored text in the terminal
import argparse
import random

# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store', dest='simple_value',
                    help='Search term')
parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')
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

# global dictionary list of terms - do not change
diction = []
subset = []
lengthmin = 6
fname = '/Users/mbpjc/projects/python-examples/assets/dictionary-list.html'
with open(fname) as f:
    diction = f.readlines()
    for term in diction:
     if len(term) > lengthmin:
          subset.append(term)
#print subset[5]
#print diction[1]

# function to get a random term from the minlength dictionary in subset list
def rando(listed):
     randomed = random.choice(listed)
     return randomed

# function that searches twitter using the public API based on searchterms set at the terminal
def gettweets(searchterms):
	tweetlist = []
	from pattern.web import Twitter, plaintext
	twitter = Twitter(language='en') 
	for tweet in twitter.search(searchterms, cached=False):
		tweetlist.append(plaintext(tweet.text))
	return tweetlist

# setup the default search terms 
searchterms = rando(subset) # default search term if none set is a random term from a dictionary list
if results.simple_value != None: # if search terms set then change from default to that
	searchterms = results.simple_value # set from argparse above in globals section

print "Search term set to: %s" % (searchterms) # Nice to see output of what random term was selected
outputtweets = gettweets(searchterms)
while len(outputtweets) == 0:
     searchterms = rando(subset)
     print "Search term set to: %s" % (searchterms)
     outputtweets = gettweets(searchterms)
if isinstance(outputtweets[0],basestring):
    outputtweets[0].encode('utf8')
else:
    unicode(outputtweets[0]).encode('utf8')
print colored('Twitter search example using pattern package:','blue')
print colored('Note: a random search term from dictionary list is set if nothing set. \n\n','red')
print outputtweets[0]
print '\n\n'
exit()


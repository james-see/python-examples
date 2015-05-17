# pattern library examples # 1
# author: James Campbell
# Date Created: 2015 05 17

import sys # need this to pass arguments at the command line
from termcolor import colored # awesome color library for printing colored text in the terminal
import argparse

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

# function that searches twitter using the public API based on searchterms set at the terminal
def gettweets(searchterms):
	tweetlist = []
	from pattern.web import Twitter, plaintext
	twitter = Twitter(language='en') 
	for tweet in twitter.search(searchterms, cached=False):
		tweetlist.append(plaintext(tweet.text))
	return tweetlist

searchterms = '"@jamescampbell"' # default search term if none set
if results.simple_value != '': # if search terms set then change from default to that
	searchterms = results.simple_value

outputtweets = gettweets(searchterms)
print colored('Twitter search example using pattern package:','blue')
print colored('Note: @jamescampbell default search term and first result returned if nothing set \n\n','yellow')
print outputtweets[1]
print '\n\n'
exit()


# pattern library examples # 1
# author: James Campbell
# Date Created: 2015 05 17

import sys
from termcolor import colored

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def gettweets(tweetlist, searchterms):
	from pattern.web import Twitter, plaintext
	twitter = Twitter(language='en') 
	for tweet in twitter.search(searchterms, cached=False):
		tweetlist.append(plaintext(tweet.text))
	return tweetlist


tweetlist = []

searchterms = '"@jamescampbell"'
if len(sys.argv) >= 2:
	searchterms = sys.argv[1]

outputtweets = gettweets(tweetlist,searchterms)
print colored('Twitter search example using pattern package:\n Note: @jamescampbell default search term and first result returned...\n\n','blue')
print outputtweets[1]
print '\n\n'
exit()


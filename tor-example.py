# tor connect example code
# author: James Campbell
# date: 2015 05 17

import socks
import socket
import urllib
import argparse
import random
import sys
import urllib.request # had to add for python 3.4 -jc

# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-o', action='store', dest='onion',
                    help='put in onion site to load (with http & quotes)') # set -o to accept onion address
results = parser.parse_args()

# Global Vars
onionsite = 'http://3g2upl4pq6kufc4m.onion' # set the default onion site to visit to test, in this case DuckDuckGo
if results.onion != None: # if search terms set in terminal then change from default to that
	onionsite = results.onion # set from argparse above in globals section

#TOR SETUP GLOBAL Vars
SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc is configured to

# Set socks proxy and wrap the urllib module
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT) # sets default proxy for connect
socket.socket = socks.socksocket # sets default socket to be the sockipy socket

# Perform DNS resolution through the socket
def getaddrinfo(*args):
  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
socket.getaddrinfo = getaddrinfo

# test connect to DuckDuckGo .onion site
headers = {'User-Agent': 'JAMES CAMPBELL jamescampbell.us SEARCH BOT! I FOUND YOU!!!!' }
	#print ('trying request now...')
req = urllib.request.Request(onionsite,None,headers)
try:
	response = urllib.request.urlopen(req) # new python 3 code -jc
	status = 'loaded successfully'
except:
	status = 'failed loading'
	currenturl = 'none'
	html =  'none'
try:
	sitehtml = response.read()
	print (sitehtml)
except urllib.error.URLError as e: 
	html = e.read().decode("utf8", 'ignore')
	#html = e.partial
	status = 'failed reading'
	html = 'none'
	currenturl = 'none'
print (status)
exit()
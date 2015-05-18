# tor connect example code
# author: James Campbell
# date: 2015 05 17

import socks
import socket
import urllib2
import argparse
import random
import sys

# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-o', action='store', dest='onion',
                    help='put in onion site to load (with http & quotes)') # set -o to accept onion address
results = parser.parse_args()

# Global Vars
onionsite = 'http://3g2upl4pq6kufc4m.onion' # set the default onion site to visit to test
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
try:
	sitehtml = urllib2.urlopen(onionsite).read()
	print sitehtml
except:
	exit('Failed to visit site, check tor connection and settings')
exit()
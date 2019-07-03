# using urllib3 ProxyManager and tor example
# author: James Campbell
# date: 2015 11 19

import socks
import socket
import urllib3  # use with python 3 only
import argparse
import random
import sys
from bs4 import BeautifulSoup

# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-o', action='store', dest='onion',
                    help='put in onion site to load (with http & quotes)')  # set -o to accept onion address
results = parser.parse_args()

# Global Vars
# set the default onion site to visit to test, in this case DuckDuckGo
onionsite = 'http://3g2upl4pq6kufc4m.onion'
if results.onion != None:  # if search terms set in terminal then change from default to that
    onionsite = results.onion  # set from argparse above in globals section

# TOR SETUP GLOBAL Vars
# TOR proxy port that is default from torrc, change to whatever torrc is configured to
SOCKS_PORT = 9050

# Set socks proxy and wrap the urllib module
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT) # sets default proxy for connect
# socket.socket = socks.socksocket # sets default socket to be the sockipy socket

# Perform DNS resolution through the socket
# def getaddrinfo(*args):
#  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
#socket.getaddrinfo = getaddrinfo
header = {'User-Agent': 'JAMES CAMPBELL jamescampbell.us SEARCH BOT! I FOUND YOU!!!!'}
# using this with privoxy and forwarding to tor, but you could use the other code above and it works fine as well
proxy = urllib3.ProxyManager('http://127.0.0.1:8119/')
r1 = proxy.request('GET', onionsite, headers=header)
print(r1.status)  # status code
print(r1.headers)  # header data
print(r1.data.decode('utf8'))  # html raw output
souper = BeautifulSoup(r1.data, "html.parser")
soupera = souper.find_all('a')  # get all a href's
for eachone in soupera:
    print('This is a link: \n', eachone.text)
exit()
# test connect to DuckDuckGo .onion site

# tor connect example code
# author: James Campbell
# date: 2015 05 17
# date updated: 2016 09 18 confirmed working (make sure to not use privoxy settings or will break)

import urllib
import urllib.request
import socks
import socket
import argparse


# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-o', action='store', dest='onion',
                    help='put in onion site to load (with http & quotes)')
results = parser.parse_args()

# Global Vars
# set the default onion site to visit to test, in this case DuckDuckGo
onionsite = 'http://3g2upl4pq6kufc4m.onion'
if results.onion is not None:  # if search terms set in terminal then change from default to that
    onionsite = results.onion  # set from argparse above in globals section

# TOR SETUP GLOBAL Vars
SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket

# Perform DNS resolution through the socket


def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]


socket.getaddrinfo = getaddrinfo

# test connect to DuckDuckGo .onion site
headers = {'User-Agent': 'JAMES CAMPBELL jamescampbell.us SEARCH BOT! I FOUND YOU!!!!'}
req = urllib.request.Request(onionsite, None, headers)
response = urllib.request.urlopen(req)  # new python 3 code -jc
status = 'loaded successfully'
try:
    sitehtml = response.read()
    print(sitehtml)
except urllib.error.URLError as e:
    html = e.read().decode("utf8", 'ignore')
    status = 'failed reading'
    html = 'none'
    currenturl = 'none'
print(status)

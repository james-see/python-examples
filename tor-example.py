# tor connect example code
# author: James Campbell
# date: 2015 05 17

import socks
import socket
import urllib2

#TOR SETUP
SOCKS_PORT = 9050  # TOR proxy port
#urlo = "http://wntxyw6zdeos7ag6.onion/" test url
# Set socks proxy and wrap the urllib module
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT) # sets default proxy for connect
socket.socket = socks.socksocket # sets default socket to be the sockipy socket
# Perform DNS resolution through the socket
def getaddrinfo(*args):
  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
socket.getaddrinfo = getaddrinfo

# test connect to DuckDuckGo .onion site
print(urllib2.urlopen('http://3g2upl4pq6kufc4m.onion').read())
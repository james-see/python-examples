# connect to i2p in python
# DATE NEW: 2015 01 21
# DATE UPDATED TO REPO: 2015 05 25
# DESCRIPTION: This is the first i2p collection tool being developed for the VIKARI toolsuite

import StringIO
import socket
import urllib
import socks  # SocksiPy module
import MySQLdb, time
from urlparse import urlparse
from bs4 import BeautifulSoup
from sys import exit
import subprocess
import shlex
import urllib2

try:
	# connect to OBSKURA database in VM
	db = MySQLdb.connect(host='localhost',user='username',passwd='password',db='your_database',port=3306)
except:
	print('database on not available, please start MYSQL to use database option, continuing...')

proxy_support = urllib2.ProxyHandler({"http":"http://127.0.0.1:4444"}) # i2p default port settings
opener = urllib2.build_opener(proxy_support) # bind proxy to urllib2
urllib2.install_opener(opener)

try:
	html = urllib2.urlopen("http://pastethis.i2p").read()
	print (html)
except: exit('no i2p connection or site is down')
if 'db' in globals(): db.close()
exit('found')
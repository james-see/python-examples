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
from termcolor import colored # awesome color library for printing colored text in the terminal

def cleanMe(html):
	soup = BeautifulSoup(html) # create a new bs4 object from the html data loaded
	for script in soup(["script", "style"]): # remove all javascript and stylesheet code
		script.extract()
	# get text
	text = soup.get_text()
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	return text

try:
	# connect to OBSKURA database in VM
	db = MySQLdb.connect(host='localhost',user='username',passwd='password',db='your_database',port=3306)
except:
	print colored('database on not available, please start MYSQL to use database option, continuing...\n', 'red')

proxy_support = urllib2.ProxyHandler({"http":"http://127.0.0.1:4444"}) # i2p default port settings
opener = urllib2.build_opener(proxy_support) # bind proxy to urllib2 for default connection setup
urllib2.install_opener(opener) #set opener as default for urllib2 object

print colored('loading example url pastethis.i2p, text of site displayed below line','green')
print ('\n------------------------\n')
try: 
	html = urllib2.urlopen("http://pastethis.i2p").read() # open the site in urllib2
	souped = cleanMe(html) # function to get text from html
	print colored(souped,'blue') # print result from parsing html
	print colored('\n\nit worked!\n\n','green') # always congratulate yourself!
except:
	print colored('Could not access site, i2p down or site is down', 'red')
	exit() # if failed, then exit early
if 'db' in globals(): db.close() # if db connected
exit()
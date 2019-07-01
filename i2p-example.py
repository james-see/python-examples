# connect to i2p in python
# DATE NEW: 2015 01 21
# DATE UPDATED TO REPO: 2019 07 01
# DESCRIPTION: Example i2p connection tool
from urllib.request import ProxyHandler, build_opener, install_opener, urlopen

from bs4 import BeautifulSoup

from termcolor import colored


def cleanMe(html):
	"""Removes all crap from html."""
	soup = BeautifulSoup(html)  # create a new bs4 object from the html data
	for script in soup(["script", "style"]):  # remove all javascript & CSS
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


proxy_support = ProxyHandler({"http": "http://127.0.0.1:4444"})  # i2p default
opener = build_opener(proxy_support)  # bind proxy to urllib2 for default
install_opener(opener)  # set opener as default for urllib2 object

print(colored('loading example url pastethis.i2p, text below', 'green'))
print('\n------------------------\n')
try: html = urlopen("http://pastethis.i2p").read()  # open the site in urllib2
except ConnectionRefusedError as e:
	print(e, "I2P may not be running, check service connection.")
	sys.exit()
souped = cleanMe(html)  # function to get text from html
print(colored(souped, 'blue'))  # print result from parsing html
print(colored('\n\nit worked!\n\n', 'green'))  # always congratulate yourself!

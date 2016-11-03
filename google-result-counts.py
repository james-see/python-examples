
import time
import requests
from bs4 import BeautifulSoup

diction = []
subset = []
fname = 'list.txt'
with open(fname) as f:
	diction = f.readlines()
	for term in diction:
		subset.append(term.strip('\n'))


#parser = argparse.ArgumentParser(description='Get Google Count.')
#parser.add_argument('word', help='word to count')
#args = parser.parse_args()

for site in subset:
	r = requests.get('http://www.google.com/search',
	                 params={'q':'"site:'+site+'"',
	                         "tbs":"li:1"}
	                )

	soup = BeautifulSoup(r.text, 'html.parser')
	print (site, soup.find('div',{'id':'resultStats'}).text)
	time.sleep(3)

exit("finis.")

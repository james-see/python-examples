import re
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from tabulate import tabulate

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
tsubset = tqdm(subset,total=len(subset))
report = ' domain name   |   total number of hits \n-------------------------------------------\n'
reporter = {"site_name":[],"results":[]}
totaler = 0 # store total results
for site in tsubset:
	tsubset.set_description("Processing %s" % site)
	r = requests.get('http://www.google.com/search',
	                 params={'q':'"site:'+site+'"',
	                         "tbs":"li:1"}
	                )

	soup = BeautifulSoup(r.text, 'html.parser')
	time.sleep(1)
	reporter["site_name"].append(site)
	results = soup.find('div',{'id':'resultStats'}).text
	reporter["results"].append(results)
	# report = report+site+' '+results+'\n'
	try: totaler = totaler + int(re.sub("[^0-9]", "", results))
	except: totaler = totaler
#print(report) # old table format
print tabulate(reporter,headers="keys",tablefmt="pipe") # awesome using tabulate
print('total pages: {}'.format(totaler))
exit("finis.")

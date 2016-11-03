
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

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
for site in tsubset:
	tsubset.set_description("Processing %s" % site)
	r = requests.get('http://www.google.com/search',
	                 params={'q':'"site:'+site+'"',
	                         "tbs":"li:1"}
	                )

	soup = BeautifulSoup(r.text, 'html.parser')
	time.sleep(3)
	report = report+site+' '+soup.find('div',{'id':'resultStats'}).text+'\n'
print(report)
exit("finis.")

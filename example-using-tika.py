import requests
import json
from pprint import pprint
#files = {'file': open('/Users/jc/Desktop/bolt-test-data/Извещение.docx', 'rb+')}

# get absolute paths and defaults
from configurator import *
import os

# globals

filelist = os.listdir(outputdir) # from configurator

for filepath in filelist:
	payload = open(filepath, 'rb').read()
	filename = filepath.rsplit('/')[0]
	print(filename)
	r = requests.put('http://localhost:9998/rmeta',data=payload)
	print(r.text)
	rdict = json.loads(r.text)[0]
	pprint(rdict['meta:page-count'])
exit()
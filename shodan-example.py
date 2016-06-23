#!/usr/bin/python
# Author: James Campbell
# Date: June 23rd 2016
# Date Updated:
# What: Shodan example

from configs import *  # have a configs.py file with shodan api key

try: import shodan
except: exit('run pip install shodan please.')

shodan_api_key = globalshodankey  # set in configs.py
try: api = shodan.Shodan(shodan_api_key)
except: exit('make sure you have the shodan key setup in configs.py as globalshodankey = "yourkey"')
try:
    results = api.count('country:GB city:Glasgow Nginx')
    if int(results['total']) == 0:
        print ('NONE FOUND! TRY AGAIN')
    else:
        print ('Results found: {}'.format(results['total']))
except:
    exit('failed')
sys.exit()

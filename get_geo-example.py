#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: James Campbell
# Date: June 23rd 2016
# Date Updated:
# What: Google API get Latitude and Longitude for address and then enrich in Shodan
from __future__ import unicode_literals

import json, urllib, sys
import urllib.parse
import urllib.request
import shodan
from configs import *


address = "4 Ferry Terminal Bldg, Kirkwall, Orkney KW15 1HU, UK"


encodedAddress = urllib.parse.quote_plus(address)
data = urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=" + encodedAddress + '&sensor=false').read().decode('utf-8')
location = json.loads(data)['results'][0]['geometry']['location']
lat = location['lat']
lng = location['lng']

# print (lat, lng)

# load lat long into shodan and see if you get any hits

shodan_api_key = globalshodankey  # set in configs.py
try: api = shodan.Shodan(shodan_api_key)
except: exit('make sure you have the shodan key setup in configs.py as globalshodankey = "yourkey"')

fullquerystring = 'geo:'+str(lat)+','+str(lng)+',5'
print(fullquerystring)
results = api.count(fullquerystring)
if int(results['total']) == 0:
        print ('NONE FOUND! TRY AGAIN')
else:
    print ('Results found: {}'.format(results['total']))

sys.exit()

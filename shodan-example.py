"""Example on using shodan api, requires shodan api key."""
# Author: James Campbell
# Date: June 23rd 2016
# Date Updated: 3 July 2019
# What: Shodan example
from configs import globalshodankey  # have a configs.py file with shodan api key
import shodan

shodan_api_key = globalshodankey  # set in configs.py
try:
    api = shodan.Shodan(shodan_api_key)
except Exception:
    exit('make sure you have the shodan key setup in configs.py as globalshodankey = "yourkey"')
try:
    results = api.count('country:GB city:Glasgow Nginx')
    if int(results['total']) == 0:
        print('NONE FOUND! TRY AGAIN')
    else:
        print(f"Results found for NGINX in Glasgow: {results['total']}")
except Exception:
    exit('failed')

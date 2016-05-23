#!/usr/bin/python

# Author: James Campbell
# Date Created: May 21st 2016
# Date Updated:
# What: Example to get stock prices

import quandl
try: from configs import *
except:
    print ('no configs file set, create a file called configs.py and add var to it like myqkey = "whatever"')
    myqkey = 'yoursecretkeyfromquandl.com'
# set API key
quandl.ApiConfig.api_key = myqkey # get free key at quandl.com
data = quandl.get("WIKI/AAPL")
print ('Total days of stock data available: {}'.format(len(data)))
#

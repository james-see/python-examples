#!/usr/bin/python

# Author: James Campbell
# Date Created: May 21st 2016
# Date Updated:
# What: Example to get stock prices

import quandl
try: from configs import *
except:
    print ('no configs file set')
    mysecretkey = 'yoursecretkeyfromquandl.com'
# set API key
quandl.ApiConfig.api_key = mysecretkey # get free key at quandl.com
data = quandl.get("APPL")

#

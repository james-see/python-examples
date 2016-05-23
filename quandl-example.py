#!/usr/bin/python

# Author: James Campbell
# Date Created: May 21st 2016
# Date Updated:
# What: Example to get stock prices
from sys import exit
try:
    import quandl
except:
    exit('quandl module required, run pip or pip3 install quandl --update')
try:
    from configs import myqkey
except:
    print('no configs file set, create a file called configs.py and add var to it like myqkey = "whatever"')
    myqkey = 'yoursecretkeyfromquandl.com'
# set API key
quandl.ApiConfig.api_key = myqkey # get free key at quandl.com
#data = quandl.get("WIKI/AAPL") # data passed into panda data table
# optional parameters can also be passed:
dataset_data = quandl.Dataset('WIKI/AAPL').data(params={ 'start_date':'2001-01-01', 'end_date':'2010-01-01', 'collapse':'annual', 'transformation':'rdiff', 'rows':4 })
print('first date: {}'.format(dataset_data[0].date))
print('Total days of stock data available: {}'.format(len(dataset_data)))
print('The data includes the following columns: {}'.format(dataset_data.column_names))

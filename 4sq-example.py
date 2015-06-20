# python example to connect and retrieve values from foursquare API
import urllib2
import urllib
import json
import datetime as dt

# globals
limiter = '1'
cityer = raw_input('What city do you want to search in? (no spaces, include country): ')
queryer = urllib.quote(raw_input('What is the name of the venue to search?: '))
clientider = '5HIGYBY4D24FXGCYTMYBUBGLYQSLORV03CRUS4E53F3GZ1VS'
clientsecreter = 'B11MC3TFDEY10XQQTUDQGGTKDGCCJBOHD4RPY5VYEW12ZNIN'
dater = dt.datetime.today().strftime("%Y%m%d")
foursquareapivenuesearch = 'https://api.foursquare.com/v2/venues/search?limit='+limiter+'&near='+cityer+'&client_id='+clientider+'&client_secret='+clientsecreter+'&v='+dater

request = urllib2.urlopen(foursquareapivenuesearch)
dataconvert = json.loads(request.read())

#print list
print(dataconvert['response'])
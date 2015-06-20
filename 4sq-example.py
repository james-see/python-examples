# python example to connect and retrieve values from foursquare API
import urllib2
import urllib # needed to do urlencode
import json
import datetime as dt

# globals
limiter = '1' # make sure to keep as string due to concat issues otherwise
cityer = raw_input('What city do you want to search in? (no spaces, include country): ')
queryer = urllib.quote(raw_input('What is the name of the venue to search?: '))
clientider = '5HIGYBY4D24FXGCYTMYBUBGLYQSLORV03CRUS4E53F3GZ1VS'
clientsecreter = 'B11MC3TFDEY10XQQTUDQGGTKDGCCJBOHD4RPY5VYEW12ZNIN'
dater = dt.datetime.today().strftime("%Y%m%d")

# the actual api call url
foursquareapivenuesearch = 'https://api.foursquare.com/v2/venues/search?limit='+limiter+'&near='+cityer+'&query='+queryer+'&client_id='+clientider+'&client_secret='+clientsecreter+'&v='+dater

request = urllib2.urlopen(foursquareapivenuesearch)
dataconvert = json.loads(request.read())

#print list of return json
print(dataconvert['response'])
lat = str(dataconvert['response']['venues'][0]['location']['lat']) # foursquare response latitude
lng = str(dataconvert['response']['venues'][0]['location']['lng']) # foursquare response longitude

#print lat long only
print('Lat/Long: '+ lat+', '+lng)

# python example to connect and retrieve values from foursquare API
import urllib2 # needed to open url
import urllib # needed to do urlencode
import json # the API call returns JSON formatted data
import datetime as dt # need date in v= or the api call doesn't work
# globals
limiter = '1' # make sure to keep as string due to concat issues otherwise
cityer = raw_input('What city do you want to search in? (no spaces, include country): ')
queryer = urllib.quote(raw_input('What is the name of the venue to search?: '))
clientider = '5HIGYBY4D24FXGCYTMYBUBGLYQSLORV03CRUS4E53F3GZ1VS'
clientsecreter = 'B11MC3TFDEY10XQQTUDQGGTKDGCCJBOHD4RPY5VYEW12ZNIN'
dater = dt.datetime.today().strftime("%Y%m%d") # the v needs YYYYMMDD format
# the actual api call url
foursquareapivenuesearch = 'https://api.foursquare.com/v2/venues/search?limit='+limiter+'&near='+cityer+'&query='+queryer+'&client_id='+clientider+'&client_secret='+clientsecreter+'&v='+dater
request = urllib2.urlopen(foursquareapivenuesearch) # open the url
dataconvert = json.loads(request.read()) # read the data returned from url
print(dataconvert['response']) # print list of return json
lat = str(dataconvert['response']['venues'][0]['location']['lat']) # foursquare response latitude
lng = str(dataconvert['response']['venues'][0]['location']['lng']) # foursquare response longitude
print('Lat/Long: '+ lat+', '+lng) # print lat long only

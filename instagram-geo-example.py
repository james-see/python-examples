# python example to connect and retrieve values from foursquare API then 
# the example gets instagram users associated with that location
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
# test print(dataconvert['response']) # print list of return json
lat = str(dataconvert['response']['venues'][0]['location']['lat']) # foursquare response latitude
lng = str(dataconvert['response']['venues'][0]['location']['lng']) # foursquare response longitude
print('Lat/Long: '+ lat+', '+lng) # print lat long only

# now take the lat/long and plug it into instagram's api for big win / beard wax
# note: would probably turn this into a function to make it noice and modular

#instagram globals
instaclientid = '35b999a6d51344cc98ebb061da538999'
instalat = lat # bring in var from foursquare call
instalong = lng # bring in var from foursquare call
instageosearch = 'https://api.instagram.com/v1/media/search?lat='+instalat+'&lng='+instalong+'&client_id='+instaclientid
instarequest = urllib2.urlopen(instageosearch)
instadataconvert = json.loads(instarequest.read())
# test print(instadataconvert) # raw json return from instagram search api
# test print str(instadataconvert['data'][0]['user']) # print first user found in json
for instauser in instadataconvert['data']:
	print instauser['user']['username']
exit()

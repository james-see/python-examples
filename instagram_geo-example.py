# python example to connect and retrieve values from foursquare API then
# the example gets instagram users associated with that location's lat/long
# Facebook killed Instagram's API so the second part does not work at all
# Date Updated: 1 July 2019
import datetime as dt  # need date in v= as YYYYMMDD
import json  # the API call returns JSON formatted data
import urllib  # needed to do urlencode
import urllib.parse
import urllib.request
# globals Foursquare API
limiter = '1'  # make sure to keep as string due to concat issues otherwise
cityer = input('What city to search? (no spaces, include country): ')
queryer = urllib.parse.quote(input('What is the name of venue to search?: '))
clientider = '5HIGYBY4D24FXGCYTMYBUBGLYQSLORV03CRUS4E53F3GZ1VS'
clientsecreter = 'B11MC3TFDEY10XQQTUDQGGTKDGCCJBOHD4RPY5VYEW12ZNIN'
dater = dt.datetime.today().strftime("%Y%m%d")  # the v needs YYYYMMDD format
# the actual api call url
foursquareapivenuesearch = f"https://api.foursquare.com/v2/venues/search?limit={limiter}&near={cityer}&query={queryer}&client_id={clientider}&client_secret={clientsecreter}&v={dater}"
request = urllib.request.urlopen(foursquareapivenuesearch)  # open the url
dataconvert = json.loads(request.read())  # read the data returned from url
lat = str(dataconvert['response']['venues'][0]['location']['lat'])
lng = str(dataconvert['response']['venues'][0]['location']['lng'])
print(f'\nLat/Long for {urllib.parse.unquote(queryer)}: {lat}, {lng} \n')

# now take the lat/long and plug it into instagram's api for big win
# note: would probably turn this into a function to make it noice and modular

# INSTAGRAM API KILLED BY FACEBOOK - FUCK YOU FACEBOOK!
print("This example was killed by Facebook killing API's. Complain to Facebook.")
# globals Instagram API
# instaclientid = '35b999a6d51344cc98ebb061da538999'
# instaaccess_token='290277.35b999a.e2423222efa04c058b0e9b95cbf77c07'
# instalat = lat # bring in var from foursquare call
# instalong = lng # bring in var from foursquare call
# instacount = '50'
# instageosearch = 'https://api.instagram.com/v1/media/search?count='+instacount+'&lat='+instalat+'&lng='+instalong+'&access_token='+instaaccess_token
# instarequest = urllib2.urlopen(instageosearch)
# instadataconvert = json.loads(instarequest.read())
# # test print(instadataconvert) # raw json return from instagram search api
# # test print str(instadataconvert['data'][0]['user']) # print first user found in json
# print ('Instagram users found at that location:\n')
# i = 0
# for instauser in instadataconvert['data']: # data is the main json object in instagram's callback
# 	username = instauser['user']['username'] # 'user' is the main json object in the data array
# 	i = i + 1
# 	print (username)
# print ('Total users found: %s' % (i))
# exit('\n\"It is not clear that intelligence has any long-term survival value - Stephen Hawking\"\n') # always end on a high note ;)
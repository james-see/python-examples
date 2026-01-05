"""Python example to connect and retrieve values from foursquare API."""
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
# Get API credentials from configs.py or environment variables
try:
    from configs import foursquare_client_id, foursquare_client_secret
    clientider = foursquare_client_id
    clientsecreter = foursquare_client_secret
except ImportError:
    import os
    clientider = os.getenv('FOURSQUARE_CLIENT_ID', '')
    clientsecreter = os.getenv('FOURSQUARE_CLIENT_SECRET', '')
    if not clientider or not clientsecreter:
        print('Error: Foursquare API credentials not found.')
        print('Please set FOURSQUARE_CLIENT_ID and FOURSQUARE_CLIENT_SECRET environment variables')
        print('or create configs.py with foursquare_client_id and foursquare_client_secret variables')
        exit(1)
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
# Note: Instagram API credentials should be loaded from configs.py or environment variables
# Example:
# try:
#     from configs import instagram_client_id, instagram_access_token
# except ImportError:
#     import os
#     instaclientid = os.getenv('INSTAGRAM_CLIENT_ID', '')
#     instaaccess_token = os.getenv('INSTAGRAM_ACCESS_TOKEN', '')
#
"""Python example to connect and retrieve values from foursquare API."""
import json  # the API call returns JSON formatted data
import datetime as dt  # need date in v= or the api call doesn't work
from urllib.parse import quote
from urllib.request import urlopen

# globals
limiter = "1"  # make sure to keep as string due to concat issues otherwise
cityer = input("What city do you want to search in? (no spaces, include country): ")
queryer = quote(input("What is the name of the venue to search?: "))
clientider = "5HIGYBY4D24FXGCYTMYBUBGLYQSLORV03CRUS4E53F3GZ1VS"
clientsecreter = "B11MC3TFDEY10XQQTUDQGGTKDGCCJBOHD4RPY5VYEW12ZNIN"
dater = dt.datetime.today().strftime("%Y%m%d")  # the v needs YYYYMMDD format
# the actual api call url
foursquareapivenuesearch = (
    "https://api.foursquare.com/v2/venues/search?limit="
    + limiter
    + "&near="
    + cityer
    + "&query="
    + queryer
    + "&client_id="
    + clientider
    + "&client_secret="
    + clientsecreter
    + "&v="
    + dater
)
request = urlopen(foursquareapivenuesearch)  # open the url
dataconvert = json.loads(request.read())  # read the data returned from url
print(dataconvert["response"])  # print list of return json
lat = str(
    dataconvert["response"]["venues"][0]["location"]["lat"]
)  # foursquare response latitude
lng = str(
    dataconvert["response"]["venues"][0]["location"]["lng"]
)  # foursquare response longitude
print(f"\nLat/Long: {lat}, {lng}")  # print lat long only
quantmapstring = f"https://www.qwant.com/maps/#map=20.08/{lat}/{lng}"
print(f"Here is the quant map page for that location:\n {quantmapstring}")
print("Right click on link and open in browser to view the location.\n")

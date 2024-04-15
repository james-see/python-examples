"""Example on how to use pinboard api using your api key and tag."""
# Note, get your api token at https://pinboard.in/settings/password
# Set the token in a configs.py file that you set pinapi = "your token"
import pinboard
from configs import pinapi
import datetime

one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
pb = pinboard.Pinboard(pinapi)  # set to your api here username:api
sec = pb.posts.all(tag=["wrk"], results=10, fromdt=one_day_ago)
for key in sec:
    print(key.description, key.tags, key.url, key.extended)

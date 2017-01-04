try: import pinboard
except: exit('must pip install pinboard first')
import datetime
# encoding=utf8
import sys
sys.path.append("..")
from pinapi import *
reload(sys)
sys.setdefaultencoding('utf8')

one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
pb = pinboard.Pinboard(pinapi) # set to your api here username:api
sec = pb.posts.all(tag=["wrk-sec"], results=10, fromdt=one_day_ago)
for key in sec:
	print(key.description, key.tags,key.url,key.extended)


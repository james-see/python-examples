# !/usr/bin/python3

import json

jsontestdata = '{"a":"red","b":"orange","c":"blue"}'

loadedjson = json.loads(jsontestdata)

for key,value in loadedjson.items(): # use .iteritems() if python 2.7
	print value
exit()
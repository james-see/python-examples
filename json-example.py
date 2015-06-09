# !/usr/bin/python3

import json

jsontestdata = '{"a":"red","b":"orange","c":"blue"}'

loadedjson = json.loads(jsontestdata)

print('iterator metod')
for key,value in loadedjson.items(): # use .iteritems() if python 2.7
	print (value)

# to show that this works as well instead of using the iterator above
print('old school method')
for value in loadedjson:
	print(loadedjson[value])
exit()
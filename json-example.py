# !/usr/bin/python3

import json
import timeit

jsontestdata = '{"a":"red","b":"orange","c":"blue"}'

loadedjson = json.loads(jsontestdata)

def itera():
	print('iterator method')
	for key,value in loadedjson.items(): # use .iteritems() if python 2.7
		print (value)

# to show that this works as well instead of using the iterator above
def iteratoo():
	print('old school method')
	for value in loadedjson:
		print(loadedjson[value])

if __name__ == '__main__':
	print(timeit.timeit("itera()",setup="from __main__ import itera")
exit()
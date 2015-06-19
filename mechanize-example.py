
# mechanize-example.py
# example showing how you can use mechanize to loop through links on a domain

import mechanize
import sys
import re

br=mechanize.Browser()

br.open('http://www.jamescampbell.us')
linklists = br.links()
print ('Total links found: ' + str(len(list(linklists))))
for j in linklists:
	print ('Base url: ' + j.base_url)
	print ('Link url: ' + j.url) 
	print ('Link text: ' + j.text)
exit()
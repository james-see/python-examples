
# mechanize-example.py
# example showing how you can use mechanize to loop through links on a domain

import mechanize
import sys
import re

br=mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('http://www.jamescampbell.us')
linklists = br.links()
print(linklists)
print ('Total links found: ' + str(len(list(linklists))))
print list(linklists)
for link in br.links():
    print link.text, link.url
exit()
# pattern-example-webcrawl.py
# pattern library example crawling jamescampbell.us
# author: James Campbell
# Date Created: 2015 05 22
# to install pattern, it is simple via pip: pip install pattern

import sys # need this to pass arguments at the command line
from termcolor import colored # awesome color library for printing colored text in the terminal
import argparse, random
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

# terminal arguments parser globals - do not change
parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store', dest='url',
                    help='Domain to crawl')
parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
results = parser.parse_args()

# setup the default search terms 
domainer = 'jamescampbell.us' # default search term if none set is a random term from a dictionary list
if results.url != None: # if search terms set then change from default to that
	domainer = results.url # set from argparse above in globals section


DOMAIN = domainer
URL = 'https://%s' % DOMAIN

class MySpider(BaseSpider):
    name = DOMAIN
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for url in hxs.select('//a/@href').extract():
            if not url.startswith('http://'):
                url= URL + url 
            print colored(url,'green')
            yield Request(url, callback=self.parse)



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

# setup the default search terms 
domainer = 'jamescampbell.us' # default search term if none set is a random term from a dictionary list
listofinternallinks = []
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
            listofinternallinks.append(url)
            print colored(url,'green')
            yield Request(url, callback=self.parse)

print len(listofinternallinks)



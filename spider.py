from __future__ import absolute_import
# getting all links example crawling jamescampbell.us
# author: James Campbell
# Date Created: 2015 05 22
# Date Updated: 2 July 2019
import argparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field

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
domainer = 'jamescampbell.us'  # default search term if none set is a random term from a dict
if results.url is not None:  # if search terms set then change from default to that
    domainer = results.url  # set from argparse above in globals section


DOMAIN = domainer
URL = 'https://%s' % DOMAIN


class MyItem(Item):
    url = Field()


class someSpider(CrawlSpider):
    name = 'crawltest'
    allowed_domains = ['jamescampbell.us']
    start_urls = ['https://jamescampbell.us']
    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self, response):
        item = MyItem()
        item['url'] = []
        for link in LxmlLinkExtractor(allow=(), deny=self.allowed_domains).extract_links(response):
            item['url'].append(link.url)
            print(link.url)
        return item


someSpider()

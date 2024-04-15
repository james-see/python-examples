"""Mechanize to loop through links on a domain."""
# Date Updated: 1 July 2019
# Author: James Campbell
import mechanize

br = mechanize.Browser()
br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1")]
br.open("http://www.jamescampbell.us")
linklists = br.links()
print(f"Total links found: {str(len(list(linklists)))} ")
print(list(linklists))
for link in br.links():
    print(link.text, link.url)

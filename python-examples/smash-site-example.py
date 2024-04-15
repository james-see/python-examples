import urllib
import urllib.request
import sys
from concurrent.futures import ThreadPoolExecutor

# globals
if len(sys.argv) < 2:
    link = 'https://jamescampbell.us'
else:
    link = sys.argv[1]

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
p = 1


def getyou(linked=link):
    global p
    f = urllib.request.Request(linked, headers=headers)
    urllib.request.urlopen(f)
    p = p + 1
    print('IM P %d' % (p,))


executor = ThreadPoolExecutor(max_workers=100)
futures = []
i = 1
while i < 500:
    a = executor.submit(getyou, link)
    futures.append(a)
    i = i + 1


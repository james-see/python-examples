import urllib
import urllib.request
from sys import exit
from concurrent.futures import ThreadPoolExecutor
link = "http://shmoocon.org"
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
p = 1
def getyou(linked=link):
    f = urllib.request.Request(linked,headers=headers)
    resp = urllib.request.urlopen(f)
    respData = resp.read()
    p = p + 1
    print('IM P %d' % (p,))

executor = ThreadPoolExecutor(max_workers=100)
futures = []
i = 1
while i < 500:
    a = executor.submit(getyou, link)
    futures.append(a)
    i = i + 1

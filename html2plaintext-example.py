"""Example on how to get plaintext from html using python's beautiful soup."""
# Author: James Campbell
# Date: 2015 05 19
# Date Updated: 2 July 2019
from bs4 import BeautifulSoup


def cleanMe(html):
    """Clean html into text only for-real."""
    soup = BeautifulSoup(html, "lxml")  # create a new bs4 object from html
    for script in soup(["script", "style"]):  # remove all javascript & css
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


testhtml = """
<!DOCTYPE HTML>\n<head>\n<title>THIS IS AN EXAMPLE by @jamescampbell</title>
    \n<meta author='jamescampbell'>\n<style>a {font-family:arial;}</style>
    \n</head><body>\n<h1>Hello World</h1>\n<p>I hope you enjoy this example.
    </p></body>
    """

print('\n\n[*-*]Before html with text:\n------------------')
print(testhtml)
print('------------------\n\n\n\n[*-*]After cleanMe() function:\n------------')
print(cleanMe(testhtml))
print('-------------------\n\n')

# python-examples
This is a collection of python examples I created for some key libraries in Python that I use all the time. 

It is a way for me to remember and hopefully get others started.

By python module:

**pattern** ([package download link](http://www.clips.ua.ac.be/pattern))
 1. [twitter search](#pattern-example) 
 2. [google search example](#google-search-example)

**bs4** ([package download link](http://www.crummy.com/software/BeautifulSoup/bs4/download/))
 1. [html to text parser](#html-to-text-example)

**socks** ([package download link](https://github.com/Anorov/PySocks))
 1. [connect to tor and print .onion site](#tor-connect-example)

**scrapy** ([package download link](http://scrapy.org/download/))
 1. [crawl all internal links for a domain](#scrapy-spider-example)

By python 3 module:
**urllib3** (package download via pip3 install urllib3 from homebrew osx brew install python3)
1. [google mask search example](#google-mask-example)

## Pattern Twitter Search Example
The first example I created is pattern-example-twitter.py. Pattern is a great library that is installed via pip and can query Google, Twitter, etc. out of the box.

This twitter example connects to twitter and searches either a random string or terms you set via the terminal with the -s 'search terms'.

Terminal Example: 

 <code>$ python pattern-example-twitter.py -s 'Hello World'</code>

## Tor Connect Example
Tor (The Onion Router) has a particular socks port and connection setup that needs configured to connect in Python. This example shows you how. You must already have [Tor](http://torproject.org/download) installed. 

*Note:* You need to install the Socksipy module for this to work, which has an actively maintained fork in [PySocks](https://github.com/Anorov/PySocks). It is easy if you already have pip (and if you don't have pip you should). <code>$ pip install PySocks</code>

Then make sure your code (like the example) has <code>import socks</code>.

#### Run the example:

Just simply run it from the terminal window:

<code>$ python tor-example.py</code>

This will return the DuckDuckGo .onion html as proof that it is working.

## Google Search Example
The Google seach portion of the pattern library is very useful. This example shows you that you can compare the popularity of phrases or sets of terms together using percentages and the sort() command. It selects 10 random words to search on from the imported included dictionary list that is in the assets folder.

#### Run the example:

<code>$ python pattern-example-google.py -c 'sexy'</code>

Returns:

<code>89.13% "sexy seemed"
2.17% "sexy impassive"
1.09% "sexy spiegels"
1.09% "sexy slumping"
1.09% "sexy quietuses"
1.09% "sexy noncooperation"
1.09% "sexy miriness"
1.09% "sexy incompliancy"
1.09% "sexy evaporators"
1.09% "sexy cudgeler"</code>

## Html to Text Example
Beautiful Soup is a great library to parse and select html or iterate through the DOM.
For this example to work you need to install Beautiful Soup via pip:
```
$ pip install bs4
```

#### Run the example:

<code>$ python example-html2plaintext.py</code>

Returns:
```
[*-*]Before html with text:
------------------
<!DOCTYPE HTML>
<head>
<title>THIS IS AN EXAMPLE by @jamescampbell</title>
<meta author='jamescampbell'>
<style>a {font-family:arial;}</style>
</head><body>
<h1>Hello World</h1>
<p>I hope you enjoy this example.</p></body>
------------------



[*-*]After cleanMe() function:
-------------------
THIS IS AN EXAMPLE by @jamescampbell
Hello World
I hope you enjoy this example.
-------------------
```

## Google Mask Example
This example does three things, 1. sets your search term, 2 . set your number of mask search terms, and 3. selects a random user agent for each search query.

#### Run the Example:
```
$ python3 mask-search-example.py
```
Returns:
```
Hello, how many terms to hide in addition to actual search term? (max 5) ?: 3
set search term: james campbell
This is a mask term: balcony
This is mask header: Dirty Dungeon Diksearch 69
This is a mask term: unrenewed
This is mask header: Internet Explorer but better
This is a mask term: gantlets
This is mask header: Mozilla/5.0
Total results: 11000000
Top 4 hits:
  http://en.wikipedia.org/wiki/James_Campbell_(industrialist)
  http://en.wikipedia.org/wiki/James_Campbell
  http://www.campbellhigh.org/
  http://www.jamescampbell.com/
For more results, see http://www.google.com/search?oe=utf8&ie=utf8&source=uds&start=0&hl=en&q=james+campbell
```

## Scrapy Spider Example
This example gets the list of all internal links for any domain by following all internal homepage links and their links.

#### Run the Example:
```
$ python spider.py -u jamescampbell.us
```

*More coming soon!*

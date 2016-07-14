# python-examples
This is a collection of python examples I created for some key libraries in Python that I use all the time. 

It is a way for me to remember and hopefully get others started.

## *By python 2.7 module:*

**pattern** ([package download link](http://www.clips.ua.ac.be/pattern))
 1. [twitter search](#pattern-example) 
 2. [google search example](#google-search-example)

**bs4** ([package download link](http://www.crummy.com/software/BeautifulSoup/bs4/download/))
 1. [html to text parser](#html-to-text-example)

**socks** ([package download link](https://github.com/Anorov/PySocks))
 1. [connect to tor and print .onion site](#tor-connect-example)

**scrapy** ([package download link](http://scrapy.org/download/))
 1. [crawl all internal links for a domain](#scrapy-spider-example)

**urllib2** ([package download link](http://pymotw.com/2/urllib2/))
 1. [access foursquare API](#foursquare-api-example)

## *By python 3.x module:* 

**rethinkdb** (install by `pip3 install rethinkdb --upgrade`)

1. [rethinkdb example](#rethinkdb-example)

**argparse** (install by `pip3 install argparse --upgrade`)

1. [argparse example](#argparse-example)

**quandl** (install by `pip3 install quandl --upgrade`)

1. [quandl api access example](#quandl-example)

**hug** (install by `pip3 install hug --upgrade`)

1. [hug api access example](#hug-example)

**base64** (package is built-in)

1. [base64 encode & decode example](#base64-example)

**http.server** (module is built-in)

1. [web server example](#server-example)

**hashlib** (package is built-in)

1. [sha 256 hash example](#sha-example)

**nltk** (module download via pip3 install nltk)

1. [sentiment analysis example](#sentiment-example)

**exifread** (module download via pip3 install exifread)

1. [read exif example](#exifread-example)

**json** (module download via pip3 install json)

1. [json to python object example](#json-to-python-object-example)

**urllib3** (module download via pip3 install urllib3 from homebrew osx brew install python3)

1. [google mask search example](#google-mask-example)
2. [urllib3 proxymanager example](#proxymanager-example)

**blockchain** (module download via pip3 install blockchain)

1. [wallet query example](#bitcoin-wallet-example)

**shodan** (module download via pip install shodan)

1. [shodan count example](#shodan-count-example)
2. [google lat/long and shodan enrichment geo search example](#google-geo-and-shodan-example)

**websockify** (module download via pip(3) install websockify)

1. [websockify example](#websockify-example)


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


## hug example
hug is a great easy-to-use api to help route things on your web app

#### Run the example:

<code>$ python3 hug_api_example.py</code>

This will output hug and start a listener process on 127.0.0.1:8000

Then you can go to http://localhost:8000/happy_birthday?name=Hug&age=1 and see the output.


## base64 Example
Converting data to base64 ensure a nice obsfuscation layer for data transport.

#### Run the example:

<code>$ python3 base64_example.py</code>

This will output a html string that is encoded into base64.


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

## Server Example   
This example starts an http server on localhost:10010 and returns data when you visit the page

#### Run the Example:   
```
$ python3 server-example.py
```

## Scrapy Spider Example
This example gets the list of all internal links for any domain by following all internal homepage links and their links.

#### Run the Example:
```
$ python3 spider.py -u jamescampbell.us
```

## Bitcoin Wallet Example
This example queries the blockchain.info API for an example wallet address and returns the ip address and dates for the transactions as well as the final wallet balance.

### Run the Example:
```
$ python3 bitcoin-example-1.py
```


## Exifread Example
This example gets the exif data from an image file

#### Run the Example:
```
$ python3 exif-reader.py assets/cat.jpg
```

#### Output:
```
Total tags found: 66
Key: Interoperability InteroperabilityVersion, value [48, 49, 48, 48]
Key: EXIF InteroperabilityOffset, value 36724
Key: Image Software, value SLT-A57 v1.02
Key: EXIF UserComment, value [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Key: Image Orientation, value Horizontal (normal)
Key: Thumbnail JPEGInterchangeFormat, value 37012
Key: Interoperability InteroperabilityIndex, value R98
Key: Image ResolutionUnit, value Pixels/Inch
Key: EXIF ExifImageWidth, value 4912
Key: EXIF ComponentsConfiguration, value YCbCr
Key: EXIF FNumber, value 28/5
Key: Thumbnail Software, value SLT-A57 v1.02
Key: EXIF DateTimeDigitized, value 2013:04:07 14:13:38
Key: EXIF ExposureProgram, value Aperture Priority
Key: EXIF DateTimeOriginal, value 2013:04:07 14:13:38
Key: EXIF Sharpness, value Normal
Key: EXIF RecommendedExposureIndex, value 3200
Key: EXIF MakerNote, value [83, 79, 78, 89, 32, 68, 83, 67, 32, 0, 0, 0, 78, 0, 3, 16, 4, 0, 16, 0, ... ]
Key: EXIF CustomRendered, value Normal
Key: EXIF Saturation, value Normal
Key: EXIF ExposureTime, value 1/80
Key: Image Make, value SONY
Key: EXIF ExifImageLength, value 3264
Key: EXIF DigitalZoomRatio, value 1
Key: Image Model, value SLT-A57
Key: EXIF Contrast, value Normal
Key: EXIF SensitivityType, value Recommended Exposure Index
Key: Thumbnail Orientation, value Horizontal (normal)
Key: Thumbnail YResolution, value 72
Key: Thumbnail Model, value SLT-A57
Key: Image PrintIM, value [80, 114, 105, 110, 116, 73, 77, 0, 48, 51, 48, 48, 0, 0, 3, 0, 2, 0, 1, 0, ... ]
Key: Thumbnail Make, value SONY
Key: EXIF CompressedBitsPerPixel, value 2
Key: EXIF MeteringMode, value Pattern
Key: EXIF MaxApertureValue, value 49/32
Key: Image YCbCrPositioning, value Co-sited
Key: EXIF BrightnessValue, value 303/320
Key: EXIF FlashPixVersion, value 0100
Key: EXIF WhiteBalance, value Auto
Key: EXIF LensModel, value 50mm F1.7
Key: Thumbnail YCbCrPositioning, value Co-sited
Key: Image DateTime, value 2013:04:07 14:13:38
Key: EXIF ExifVersion, value 0230
Key: Thumbnail ImageDescription, value                                
Key: Image ExifOffset, value 360
Key: Thumbnail JPEGInterchangeFormatLength, value 7654
Key: EXIF ExposureMode, value Auto Bracket
Key: EXIF SceneType, value Directly Photographed
Key: EXIF LensSpecification, value [50, 50, 17/10, 17/10]
Key: Image XResolution, value 350
Key: EXIF ExposureBiasValue, value 0
Key: EXIF ColorSpace, value sRGB
Key: EXIF ISOSpeedRatings, value 3200
Key: EXIF SceneCaptureType, value Standard
Key: EXIF FocalLengthIn35mmFilm, value 75
Key: Image YResolution, value 350
Key: Thumbnail DateTime, value 2013:04:07 14:13:38
Key: EXIF FocalLength, value 50
Key: Thumbnail Compression, value JPEG (old-style)
Key: EXIF FileSource, value Digital Camera
Key: EXIF Flash, value Flash did not fire, compulsory flash mode
Key: Image ImageDescription, value                                
Key: Thumbnail XResolution, value 72
Key: Thumbnail ResolutionUnit, value Pixels/Inch
Key: EXIF LightSource, value Unknown
```

## Sentiment Example
This example takes a test list of tweets and returns positive or negative. It works in Python 3.

#### Run the Example:
```
$ python3 sentiment-analysis-nltk-example.py testtweets.txt
```

#### Output:
```
negative
positive
negative
positive
negative
Positive count: 2
Negative count: 3
```

## hashlib example
The hashlib module generates hashes from strings. This example uses the sha256 hash algorithm.

#### Run the Example:

```
$ python3 hashlib_example.py
```

## Proxymanager Example
This example uses urllib3 in Python 3 to connect through a privoxy connection and return status, headers, and content.

#### Run the Example:
```
$ python3 urllib3-proxymanager-example.py
```

#### Output:
```
200
HTTPHeaderDict({'Content-Length': '5255', 'Proxy-Connection': 'keep-alive', 'ETag': '"564e8118-1487"', 'Server': 'nginx', 'Cache-Control': 'no-cache', 'Expires': 'Fri, 20 Nov 2015 02:15:59 GMT', 'Accept-Ranges': 'bytes', 'Content-Type': 'text/html; charset=UTF-8', 'Connection': 'keep-alive', 'Date': 'Fri, 20 Nov 2015 02:16:00 GMT'})
<!DOCTYPE html>
<!--[if IEMobile 7 ]> <html lang="en_US" class="no-js iem7"> <![endif]-->
<!--[if lt IE 7]> <html class="ie6 lt-ie10 lt-ie9 lt-ie8 lt-ie7 no-js" lang="en_US"> <![endif]-->
<!--[if IE 7]>    <html class="ie7 lt-ie10 lt-ie9 lt-ie8 no-js" lang="en_US"> <![endif]-->
<!--[if IE 8]>    <html class="ie8 lt-ie10 lt-ie9 no-js" lang="en_US"> <![endif]-->
<!--[if IE 9]>    <html class="ie9 lt-ie10 no-js" lang="en_US"> <![endif]-->
<!--[if (gte IE 9)|(gt IEMobile 7)|!(IEMobile)|!(IE)]><!--><html class="no-js" lang="en_US"><!--<![endif]-->

  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8;charset=utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=1" />
<meta name="HandheldFriendly" content="true"/>

<link rel="canonical" href="https://duckduckgo.com/">

<link rel="stylesheet" href="/s1049.css" type="text/css">
<link rel="stylesheet" href="/t1049.css" type="text/css">


<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" sizes="16x16 24x24 32x32 64x64"/>
<link rel="apple-touch-icon" href="/assets/icons/meta/DDG-iOS-icon_60x60.png"/>
<link rel="apple-touch-icon" sizes="76x76" href="/assets/icons/meta/DDG-iOS-icon_76x76.png"/>
<link rel="apple-touch-icon" sizes="120x120" href="/assets/icons/meta/DDG-iOS-icon_120x120.png"/>
<link rel="apple-touch-icon" sizes="152x152" href="/assets/icons/meta/DDG-iOS-icon_152x152.png"/>
<link rel="image_src" href="/assets/icons/meta/DDG-icon_256x256.png"/>

<link title="DuckDuckGo" type="application/opensearchdescription+xml" rel="search" href="/opensearch.xml">

<meta name="twitter:site" value="@duckduckgo">
<meta name="twitter:url" value="https://duckduckgo.com/">

<meta property="og:url" content="https://duckduckgo.com/" />
<meta property="og:site_name" content="DuckDuckGo" />


	<title>DuckDuckGo</title>
<meta property="og:title" content="DuckDuckGo" />
<meta name="twitter:title" value="DuckDuckGo">


<meta name="description" content="The search engine that doesn't track you. A superior search experience with smarter answers, less clutter and real privacy.">


  </head>
  <body id="pg-index" class="page-index body--home">
	<script type="text/javascript">
var settings_js_version = "/s1847.js",
    locale = "en_US";
</script>
<script type="text/javascript" src="/locales/en_US/LC_MESSAGES/duckduckgo-duckduckgo+sprintf+gettext+locale-simple.20151112.063921.js"></script>
<script type="text/javascript" src="/d1847.js"></script>


<script type="text/javascript">
    DDG.page = new DDG.Pages.Home();
</script>



	<div class="site-wrapper  site-wrapper--home  js-site-wrapper">

		<div class="site-wrapper-border"></div>



			<div class="header-wrap--home  js-header-wrap"></div>

			<div id="" class="content-wrap--home">
			  <div id="content_homepage" class="content--home">
				<div class="cw--c">
							<div class="logo-wrap--home">
			<a id="logo_homepage_link" class="logo_homepage" href="/about">
				About DuckDuckGo
				<span class="logo_homepage__tt">Duck it!</span>
			</a>
		</div>

					<div class="search-wrap--home">
								<form id="search_form_homepage" class="search  search--home  js-search-form" name="x" method="POST" action="/html">
			<input id="search_form_input_homepage" class="search__input  js-search-input" type="text" autocomplete="off" name="q" tabindex="1" value="">
			<input id="search_button_homepage" class="search__button  js-search-button" type="submit" tabindex="2" value="S" />
			<input id="search_form_input_clear" class="search__clear  empty  js-search-clear" type="button" tabindex="3" value="X" />
			<div id="search_elements_hidden" class="search__hidden  js-search-hidden"></div>
			<span class="search__overlay  js-search-overlay"></span>
		</form>

					</div>




		<!-- en_US All Settings -->
<noscript>
	<div class="tag-home">
		The search engine that doesn't track you.
		<span class="tag-home__links">
			<span class="js-homepage-cta"><a href="/spread" class="tag-home__link">Help Spread DuckDuckGo!</a> <span class="tag-home__links__sep">|</span> </span><a href="/tour" class="tag-home__link">Take a Tour</a>
		</span>
	</div>
</noscript>
<div class="tag-home  tag-home--slide  no-js__hide  js-tag-home"></div>
		<div id="error_homepage"></div>




				</div> <!-- cw -->
			 </div> <!-- content_homepage //-->
		  </div> <!-- content_wrapper_homepage //-->
		  <div id="footer_homepage" class="foot-home  js-foot-home"></div>

<script type="text/javascript">
	{function seterr(str) {
		var error=document.getElementById('error_homepage');
		error.innerHTML=str;
		$(error).css('display','block');
	}
	var err=new RegExp('[\?\&]e=([^\&]+)');var errm=new Array();errm['2']='no search';errm['3']='search too long';errm['4']='not UTF\u002d8 encoding';if (err.test(window.location.href)) seterr('Oops, '+(errm[RegExp.$1]?errm[RegExp.$1]:'there was an error.')+' &nbsp;Please try again');};if (ip) setTimeout('nuo(1)',250);nip(1)

	if (kurl) {
	  document.getElementById("logo_homepage_link").href += (document.getElementById("logo_homepage_link").href.indexOf('?')==-1 ? '?t=i' : '') + kurl;
	}
</script>




    </div> <!-- site-wrapper -->
  </body>
</html>

This is a link:

				About DuckDuckGo
				Duck it!

This is a link:
 Help Spread DuckDuckGo!
This is a link:
 Take a Tour
```

## Quandl Example   
This example gets the stocks from AAPL into a dataframe and prints it.   

#### Run the Example:
```
$ python3 quandl-example.py
```

#### Output:

```
$ first date: 2001-12-31
$ Total days of stock data available: 4
$ [Finished in 1.6s]
```

## Json to Python Object Example
This example takes a json object and converts it to python and iterates through the values. It works for Python 3 or Python 2.7

#### Run the Example:
```
$ python3 json-example.py 
```

## Foursquare API Example
This example connects to Foursquare and asks for a city, country input and venue name and returns back the JSON and the Latitude and Longitude.

#### Run the Example:
```
$ python 4sq-example.py
```

#### Output:
```
What city do you want to search in? (no spaces, include country): London,UK
What is the name of the venue to search?: Millenium Hotel
{
    u'geocode': {
        u'parents': [
            
        ],
        u'what': u'',
        u'where': u'londonuk',
        u'feature': {
            u'highlightedName': u'<b>London</b>,
            GreaterLondon,
            <b>UK</b>',
            u'displayName': u'London,
            GreaterLondon,
            UnitedKingdom',
            u'name': u'London',
            u'longId': u'72057594040571679',
            u'cc': u'GB',
            u'id': u'geonameid: 2643743',
            u'geometry': {
                u'center': {
                    u'lat': 51.50853,
                    u'lng': -0.12574
                },
                u'bounds': {
                    u'sw': {
                        u'lat': 51.28467404417054,
                        u'lng': -0.5085579279369435
                    },
                    u'ne': {
                        u'lat': 51.691643999655895,
                        u'lng': 0.33418999705203406
                    }
                }
            },
            u'matchedName': u'London,
            GreaterLondon,
            UK',
            u'woeType': 7,
            u'slug': u'london'
        }
    },
    u'venues': [
        {
            u'verified': True,
            u'name': u'MillenniumHotelLondonMayfair',
            u'referralId': u'v-1434850451',
            u'url': u'http: //www.millenniumhotels.co.uk',
            u'storeId': u'',
            u'hereNow': {
                u'count': 0,
                u'groups': [
                    
                ],
                u'summary': u'Nobodyhere'
            },
            u'specials': {
                u'count': 0,
                u'items': [
                    
                ]
            },
            u'contact': {
                u'facebookName': u'Millennium&CopthorneHotelsEurope',
                u'twitter': u'millenniumeu',
                u'phone': u'+442076299400',
                u'facebook': u'456685494411593',
                u'formattedPhone': u'+442076299400',
                u'facebookUsername': u'MillenniumEU'
            },
            u'location': {
                u'city': u'Mayfair',
                u'cc': u'GB',
                u'country': u'UnitedKingdom',
                u'postalCode': u'W1K2HP',
                u'state': u'GreaterLondon',
                u'formattedAddress': [
                    u'44GrosvenorSquare',
                    u'Mayfair',
                    u'GreaterLondon',
                    u'W1K2HP',
                    u'UnitedKingdom'
                ],
                u'address': u'44GrosvenorSquare',
                u'lat': 51.51086806955976,
                u'lng': -0.1512632169763817
            },
            u'stats': {
                u'tipCount': 31,
                u'checkinsCount': 3586,
                u'usersCount': 1559
            },
            u'id': u'4ac518b5f964a52090a020e3',
            u'categories': [
                {
                    u'pluralName': u'Hotels',
                    u'primary': True,
                    u'name': u'Hotel',
                    u'shortName': u'Hotel',
                    u'id': u'4bf58dd8d48988d1fa931735',
                    u'icon': {
                        u'prefix': u'https: //ss3.4sqi.net/img/categories_v2/travel/hotel_',
                        u'suffix': u'.png'
                    }
                }
            ]
        }
    ]
}

Lat/Long: 51.5108680696, -0.151263216976
```

## argparse Example   
This example sets some basic args. 

#### Run the Example:

```
$ python3 argparse.py -h
```
Returns:

```
usage: argparse example [-h] [-a] [-v] [--verbose]

Example on how to use argparse

positional arguments:
  +a             Turn A on

optional arguments:
  -h, --help     show this help message and exit
  -a             Turn A off
  -v, --version  show program's version number and exit
  --verbose      verbose flag
```

## Shodan Count Example   
This example connects to shodan api via your configs.py file with proper api key variable set and then queries for nginx in Glasgow, GB.

#### Run the Example:   
```
python3 shodan-example.py
```

#### Returns:

```
Results found: 246
[Finished in 0.6s]
```

## Google GEO and Shodan Example   
This example takes an address, gets the lat/long, and searches in shodan for matches near that location.

#### Run the Example:   
```
python3 get-geo-example.py
```

#### Returns:

```
geo:58.98691099999999,-2.960873,3
Results found: 572
[Finished in 0.7s]
```

## RethinkDB Example
This example takes pastebin archive daily json data into a test table in rethinkdb and pulls out values from it.

#### Run the Example:    
```
python3 rethink-example.py
```

#### Returns:


## Websockify Example   
This example uses websockify.   
```
python3 websockify-example.py :8015 :80
```

#### Returns:



*More coming soon!*


# python-examples
This is a collection of python examples I created for some key libraries in Python that I use all the time. 

It is a way for me to remember and hopefully get others started.

*By python 2.7 module:*

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

*By python 3.4 module:* 

**urllib3** (pacakge download via pip3 install urllib3)

1. [urllib3 proxymanager example](#proxymanager-example)

**nltk** (package download via pip3 install nltk)

1. [sentiment analysis example](#sentiment-example)

**exifread** (package download via pip3 install exifread)

1. [read exif example](#exifread-example)

**json** (package download via pip3 install json)

1. [json to python object example](#json-to-python-object-example)

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
$ python3 spider.py -u jamescampbell.us
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

## Proxymanager Example
This example uses urllib3 in Python 3 to connect through a privoxy connection and return status, headers, and content.

#### Run the Example:
```
$ python3 urllib3-proxymanager-example.py
```

#### Output:


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

*More coming soon!*


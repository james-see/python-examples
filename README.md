# python-examples
Examples for some key libraries in Python that I use all the time. A way for me to remember and hopefully get others started.

## Pattern Example
The first example I created is pattern-example-twitter.py. Pattern is a great library that is installed via pip and can query Google, Twitter, etc. out of the box.

This twitter example connects to twitter and searches either a random string or terms you set via the terminal with the -s 'search terms'.

Terminal Example: 

 <code>$ python pattern-example-twitter.py -s 'Hello World'</code>

## Tor Connect Example
Tor (The Onion Router) has a particular socks port and connection setup that needs configured to connect in Python. This example shows you how. You must already have [Tor](http://torproject.org/download) installed. 

*Note:* You need to install the Socksipy module for this to work, which has an actively maintained fork in [PySocks](https://github.com/Anorov/PySocks). It is easy if you already have pip (and if you don't have pip you should). <code>$ pip install PySocks</code>

Then make sure your code (like the example) has <code>import socks</code>.

### Run the example:

Just simply run it from the terminal window:

<code>$ python tor-example.py</code>

This will return the DuckDuckGo .onion html as proof that it is working.

## Google Search Example
The Google seach portion of the pattern library is very useful. This example shows you that you can compare the popularity of phrases or sets of terms together using percentages and the sort() command. It selects 10 random words to search on from the imported included dictionary list that is in the assets folder.

Terminal Example:

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


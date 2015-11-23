# author: James Campbell
# what: example three+ categorization of tweets using nltk
# date created: November 23 2015
import nltk
import sys
from sys import exit

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('Going well', 'positive'),
              ('Thank you', 'positive'),
              ('Hope you are doing well', 'positive'),
              ('I am very happy', 'positive'),
              ('Good for you', 'positive'),
              ('all good. I know about it and I accept it.', 'positive'),
              ('This is really good!', 'positive'),
              ('Tomorrow is going to be fun.', 'positive'),
              ('Smiling all around.', 'positive'),
              ('These are great apples today.', 'positive'),
              ('How about them apples? Thomas is a happy boy.', 'positive'),
              ('Thomas is very zen. He is well-mannered.', 'positive'),
              ('happy and good lots of light!', 'positive'),
              ('I like this new iphone very much', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('I am a bad boy', 'negative'),
              ('This is not good', 'negative'),
              ('I am bothered by this', 'negative'),
              ('I am not connected with this', 'negative'),
              ('Sadistic creep you ass. Die.', 'negative'),
              ('All sorts of crazy and scary as hell.', 'negative'),
              ('Not his emails, no.', 'negative'),
              ('His father is dead. Returned obviously.', 'negative'),
              ('He has a bomb.', 'negative'),
              ('Too fast to be on foot. We cannot catch them.', 'negative'),
              ('Feeling so stupid stoopid stupid!', 'negative'),
              (':-(( :-(', 'negative'),
              ('This is the worst way imaginable, all of this traffic', 'negative')]

rain_tweets = [('this rain is craze today', 'rain'),
               ('Nov 23 17:30 Temperature 3C no or few clouds Wind SW 6 km/h  Humidity 70% France', 'rain'),
               ('missin climbing mountains in the rain', 'rain'),
               ('There are days in live broadcasting Torrential rain in Paris ', 'rain'),
               ('Heavy Rain today in!', 'rain'),
               ('Woman in the boulangerie started complaining about the rain. I said, "its better than terrorists". Need to finesse my jovial patter', 'rain'),
               ('Light to moderate rain over NCR', 'rain'),
               ('After a cold night last night, tonight will be milder and mainly frost-free, with this band of rain. Jo', 'rain'),
               ('But I love the rain. And it rains frequently these days~ So it makes me feel rather good', 'rain'),
               ('With 1000 mm rain already and more rain forecasted 4 Chennai, Nov 2015 will overtake Oct 2005 and Nov 1918 to become the Wettest Month EVER!', 'rain'),
               ('It is raining today. Wet!', 'rain'),
               ('Lots of rain today. Raining!', 'rain'),
               ('Why is it raining?', 'rain'),
               ('So much rain!', 'rain'),
               ('it always rains this time of year', 'rain'),
               ('raining', 'rain'),
               ('raining outside today, rained yesterday too', 'rain'),
               ('rainy weather today! jeez', 'rain'),
               ('Rain has finally extinguished a #wildfire in Olympic National Park that had been burning since May', 'rain'),
               ('The rain had us indoors for Thursdays celebration', 'rain'),
               ('Rain (hourly) 0.0 mm, Pressure: 1012 hPa, falling slowly', 'rain'),
               ('That aspiration yours outfit make ends meet spite of the rainy weather this midsummer?: Edb', 'rain'),
               ('Glasgow\'s bright lights of Gordon st tonight #rain #Glasgow', 'rain'),
               ('Why is it raining? Because it always rains this time of year', 'rain'),
               ('The forecast for this week\'s weather includes lots of rain!', 'rain')]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets + rain_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 2]
    tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

word_features = get_word_features(get_words_in_tweets(tweets))

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

runtweets = []  # setup to import a list of tweets here if you wish into a python list
if len(sys.argv) > 1:  # if param passed 4 name of text file w/ list of tweets
    tweetfile = sys.argv[1]
    with open(tweetfile, "r") as ins:
      for line in ins:
        runtweets.append(line)
runtweets.append('I am a bad boy')  # should be negative
runtweets.append('rain today')  # should be rain
runtweets.append('so stupid')  # should be negative
runtweets.append('it is raining outside')  # should be rain
runtweets.append('I love it')  # should be positive
runtweets.append('so good')  # should be positive
poscount = 0
negcount = 0
raincount = 0
for tweett in runtweets:
  valued = classifier.classify(extract_features(tweett.split()))
  print (valued)
  if valued == 'negative':
    negcount = negcount + 1
  if valued == 'positive':
    poscount = poscount + 1
  if valued == 'rain':
    raincount = raincount + 1
print ('Positive count: %s \nNegative count: %s \nRain count: %s' % (poscount, negcount, raincount))
exit()

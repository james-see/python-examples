#!/usr/bin/python3
# Author: James Campbell
# Date: November 11 2016
# What: Example using nltk tokenize and ngrams
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import re, string

def get_ngrams(text, n ):
    l = word_tokenize(text)
    ll = [x for x in l if not re.fullmatch('[' + string.punctuation + ']+', x)]
    ll = ngrams(ll,n)
    return [ ' '.join(grams) for grams in ll]

ngramer = get_ngrams("This is a sentence to parse out ngrams for it.",4)
for gram in ngramer:
    print(gram)

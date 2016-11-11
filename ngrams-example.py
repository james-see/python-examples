#!/usr/bin/python3
# Author: James Campbell
# Date: November 11 2016
# What: Example using nltk tokenize and ngrams

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]

get_ngrams("This is a sentence to parse out ngrams for it.",4)

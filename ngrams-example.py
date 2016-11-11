#!/usr/bin/python3
# Author: James Campbell
# Date: November 11 2016
# What: Example using nltk tokenize and ngrams

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def get_ngrams(text, n ):
    l = nltk.word_tokenize(text)
    ll = [x for x in l if not re.fullmatch('[' + string.punctuation + ']+', x)]
    n_grams = ngrams(word_tokenize(ll), n)
    return [ ' '.join(grams) for grams in n_grams]

ngramer = get_ngrams("This is a sentence to parse out ngrams for it.",4)
for gram in ngramer:
    print(gram)

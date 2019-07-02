"""Example to use fuzzywuzzy which does a fuzzy match fast."""
# Author: James Campbell
# Date: August 11th 2016
# Date Updated: 2 July 2019

from fuzzywuzzy import process

choices = ["Atlanta Falcons", "New York Jets", "Dallas Cowboys"]
hello = process.extractOne("cowboys", choices)
print(hello)  # should print Dallas Cowboys

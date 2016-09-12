# Author: James Campbell
# What: Example to use fuzzywuzzy which does a fuzzy match fast
# Date: August 11th 2016

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
hello = process.extractOne("cowboys", choices)
print(hello) # should print Dallas Cowboys


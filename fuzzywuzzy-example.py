from fuzzywuzzy import fuzz
from fuzzywuzzy import process

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
hello = process.extractOne("cowboys", choices)
print(hello)

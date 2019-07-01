"""Example on how to use json."""
# Date Updated: 1 July 2019
import json
jsontestdata = '{"a":"red","b":"orange","c":"blue"}'
loadedjson = json.loads(jsontestdata)


def itera():
    """Quick method iterator."""
    print('iterator method')
    for _, value in loadedjson.items():  # use .iteritems() if python 2.7
        print(value)

# to show that this works as well instead of using the iterator above


def iteratoo():
    """Old school method."""
    print('old school method')
    for value in loadedjson:
        print(loadedjson[value])


itera()
iteratoo()

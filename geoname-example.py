"""Shows how to use geotext."""
from geotext import GeoText

places = GeoText("London is a great city")
places.cities
# "London"

# filter by country code
result = GeoText('I loved Rio de Janeiro and Havana', 'BR').cities
print(result)
# 'Rio de Janeiro'

print(GeoText('New York, Texas, and also China').country_mentions)
# OrderedDict([(u'US', 2), (u'CN', 1)])

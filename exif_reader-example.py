"""Show how to get exif data."""
import sys
from PIL import Image, ExifTags

try:
    import exifread
except ModuleNotFoundError as e:
    print(e, "pip3 install this!")
    exit(1)
try:
    import iptcinfo
except ModuleNotFoundError as e:
    print(e, "pip3 install this!")
    exit(1)

# Open image file for reading (binary mode)
path_name = 'assets/cat.jpg'
try:
    f = sys.argv[1]  # check to see if image in command line
    f = open(f, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
totaltags = len(tags)
print ('-------EXIF DATA FOUND-------')
print ('Total EXIF tags found: %s' % (totaltags,))
for tag in tags.keys():
	print ("Key: %s, value %s" % (tag, tags[tag]))
print ('-----------------END EXIF DATA-------')

im = Image.open(sys.argv[1])
try:
    iptc = iptcinfo.IPTCInfo(sys.argv[1])

    image_title = iptc.data.get('object name', '') or iptc.data.get('headline', '')
    image_description = iptc.data.get('caption/abstract', '')
    image_tags = iptc.keywords
    print (image_description)
    print (image_tags)
    print(image_title)

except Exception as e:
    if str(e) != "No IPTC data found.":
        raise
print ('--------START OF PY3exiv2 DATA----------')
data = py3exiv2.metadata.ImageMetadata(sys.argv[1])
data.read()
for key in data.exif_keys:
    tag = data[key]
    print(' %-40s%s' %(key, tag.value))
print ('-------END PY3exiv2 DATA-----------')
sys.exit()

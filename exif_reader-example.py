"""Show how to get exif data and iptc data from various libraries."""
import sys
from PIL import Image, ExifTags


try:
    import exifread
except ModuleNotFoundError as e:
    print(e, "pip3 install this!")
    exit(1)
try:
    import iptcinfo3
except ModuleNotFoundError as e:
    print(e, "pip3 install this!")
    exit(1)

# Open image file for reading (binary mode)
path_name = 'assets/cat.jpg'
f = sys.argv[1]  # check to see if image in command line
f = open(f, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
totaltags = len(tags)
print('-------EXIF DATA FOUND-------')
print(f"Total EXIF tags found: {totaltags}")
for tag in tags.keys():
    print("Key: %s, value %s" % (tag, tags[tag]))
print('-----------------END EXIF DATA-------')

im = Image.open(sys.argv[1])
try:
    info = iptcinfo3.IPTCInfo(sys.argv[1])
    print('-------IPTC DATA FOUND-------')
    for k, v in info._data.items():
        print(k, v)
    info['city'] = '#magistræde #🇩🇰'
    info.save()
except Exception as e:
    if str(e) != "No IPTC data found.":
        raise


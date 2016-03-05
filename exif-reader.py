from PIL import Image, ExifTags
import sys
try:
    import exifread
except:
    exit('install exifread via pip to have this work properly')
# pip install iptcinfo
try:
    import iptcinfo
except:
    exit('install iptcinfo via pip to have this work properly')
# Open image file for reading (binary mode)
path_name = 'assets/cat.jpg'
try:
    f = sys.argv[1] # check to see if image in command line
    f = open(f, 'rb')
except:
    try:
        f = open(path_name, 'rb')
    except:
        exit('failed to open file, check path settings or put full path and image')
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


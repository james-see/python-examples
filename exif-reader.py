import exifread
# Open image file for reading (binary mode)
path_name = 'assets/cat.jpg'
try:
	f = open(path_name, 'rb')
except:
	exit('failed to open file, check path settings')

# Return Exif tags
tags = exifread.process_file(f)
totaltags = len(tags)
print ('Total tags found: %s' % (totaltags,))
for tag in tags.keys():
	print ("Key: %s, value %s" % (tag, tags[tag]))

import exifread
# Open image file for reading (binary mode)
path_name = 'assets/exif-example.jpg'
try:
	f = open(path_name, 'rb')
except:
	exit('failed to open file, check path settings')

# Return Exif tags
tags = exifread.process_file(f)
for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print ("Key: %s, value %s" % (tag, tags[tag]))

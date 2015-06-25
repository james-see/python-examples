# djvu to pdf & pdf ocr script example
# requirements = djvu2pdf (brew install djvu2pdf on osx with homebrew installed)
import sys, os
import subprocess
import fnmatch

# globals

inputfolderpath = '/Users/mbpjc/projects/biblio/' # set this to your input folder path
# outputpath = '/Users/mbpjc/projects/biblio/output/'
operationtype = raw_input('Input from folder (1) or single file (2)?: ')

# functions
# this function finds specific files in a directory
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

# if you are doing this on an entire folder then
if operationtype == '1':
	i = 0
	for filename in find_files(inputfolderpath,'*.djvu'):
		print ('Processing %s...' % filename)
		i = i + 1
		p = subprocess.Popen(["djvu2pdf", filename], stdout=subprocess.PIPE) 
		output, err = p.communicate()
		#subprocess.call(["djvu2pdf", filename])
		print('Processing finished for %s' % filename)
	print ('processed %s file(s)' % i)
	exit('\n\"Sanity is madness put to good uses.\" - George Santayana\n')

# if you are processing just a single file then
if operationtype == '2':
	filename = raw_input('What filename to process? (must be in same directory): ')
	if 'djvu' in filename: 
		print('Processing DJVU to PDF...')
		p = subprocess.Popen(["djvu2pdf", filename], stdout=subprocess.PIPE) 
		output, err = p.communicate()
		#subprocess.call(["djvu2pdf", filename])
		print('Processing finished')
		exit('Completed sucessfully')


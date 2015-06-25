# djvu to pdf script example
# requirements = djvu2pdf (brew install djvu2pdf on osx with homebrew installed)
# or install it on Ubuntu / Debian sudo apt-get install djvulibre-bin ghostscript
import sys, os
import subprocess
import fnmatch

# globals

inputfolderpath = '/Users/mbpjc/projects/biblio/' # set this to your input folder path
outputpath = '/Users/mbpjc/projects/biblio/output/' # set to output folder (must exist)
operationtype = raw_input('Input from folder (1) or single file (2)?: ')

# functions
# this function finds specific files in a directory
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = basename
                yield filename

# if you are doing this on an entire folder then
if operationtype == '1':
	i = 0
	for filename in find_files(inputfolderpath,'*.djvu'):
		print ('[*] Processing DJVU to PDF for %s...' % filename)
		i = i + 1
		inputfull = inputfolderpath+filename
		outputfilename = filename[:-4]+'pdf'
		outputfilepath = outputpath
		p = subprocess.Popen(["djvu2pdf", inputfull], stdout=subprocess.PIPE) 
		output, err = p.communicate()
		subprocess.call(["mv", outputfilename, outputfilepath])
		print('[-] Processing finished for %s' % filename)
	print ('[--] processed %s file(s) [--]' % i)
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
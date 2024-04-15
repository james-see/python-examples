"""djvu to pdf script example."""
# Date Updated: 1 July 2019
# pre-req osx: djvu2pdf (brew install djvu2pdf with homebrew installed)
# pre-req Ubuntu / Debian: sudo apt-get install djvulibre-bin ghostscript
import fnmatch
import os
import subprocess
# global variables (change to suit your needs)
inputfolderpath = '~'  # set to import folder path
outputpath = '~'  # set to output folder (must exist)
operationtype = input('Input from folder (1) or single file (2)?: ')


def find_files(directory, pattern):
    """Find specific files in a directory and sub directories."""
    for _, _, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = basename
                yield filename


if operationtype == '1':
    i = 0
    print(f"Input dir & sub directory underneath set as {inputfolderpath}")
    for filename in find_files(inputfolderpath, '*.djvu'):
        print(f"[*] Processing DJVU to PDF for {filename}...")
        i = i + 1
        inputfull = inputfolderpath+filename
        outputfilename = filename[:-4]+i+'pdf'  # make filename unique
        outputfilepath = outputpath
        p = subprocess.Popen(["djvu2pdf", inputfull], stdout=subprocess.PIPE)
        output, err = p.communicate()
        subprocess.call(["mv", outputfilename, outputfilepath])
        print('[-] Processing finished for %s' % filename)
    print(f"[--] processed {i} file(s) [--]")
    exit('\n\"Sanity is madness put to good uses.\" - George Santayana\n')

elif operationtype == '2':
    filename = input('What filename to process? (leave blank for example): ')
    if 'djvu' in filename:
        print('Processing DJVU to PDF...')
        p = subprocess.Popen(["djvu2pdf", filename], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print('Processing finished')
        exit('Completed sucessfully')
    else:
        print('No djvu file to process, running sample')
        print('Processing DJVU to PDF...')
        p = subprocess.Popen(["djvu2pdf", "assets/example.djvu"],
                             stdout=subprocess.PIPE)
        output, err = p.communicate()
        print('Processing finished')
        exit('Completed sucessfully')


elif operationtype == '':
    exit('You hit enter without inputing anything, nice work, exiting.')

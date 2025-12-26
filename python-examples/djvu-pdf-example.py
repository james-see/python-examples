"""djvu to pdf script example."""
# Date Updated: 1 July 2019
# pre-req osx: djvu2pdf (brew install djvu2pdf with homebrew installed)
# pre-req Ubuntu / Debian: sudo apt-get install djvulibre-bin ghostscript
import fnmatch
import os
import subprocess
import shutil
from pathlib import Path
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
        inputfull = os.path.join(inputfolderpath, filename)
        # Validate that the file exists and is a regular file
        if not os.path.isfile(inputfull):
            print(f"[!] Skipping {filename} - not a valid file")
            continue
        outputfilename = f"{filename[:-5]}_{i}.pdf"  # make filename unique
        outputfilepath = os.path.join(outputpath, outputfilename)
        # Use list for subprocess to avoid shell injection
        p = subprocess.Popen(
            ["djvu2pdf", inputfull],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, err = p.communicate()
        # Use shutil.move instead of shell command for better security
        if p.returncode == 0 and os.path.exists(outputfilename):
            shutil.move(outputfilename, outputfilepath)
        print('[-] Processing finished for %s' % filename)
    print(f"[--] processed {i} file(s) [--]")
    exit('\n\"Sanity is madness put to good uses.\" - George Santayana\n')

elif operationtype == '2':
    filename = input('What filename to process? (leave blank for example): ')
    if filename and 'djvu' in filename:
        # Validate filename to prevent path traversal
        safe_path = Path(filename).resolve()
        if not safe_path.is_file() or not str(safe_path).endswith('.djvu'):
            print('[!] Invalid file or not a .djvu file')
            exit('Invalid input')
        print('Processing DJVU to PDF...')
        p = subprocess.Popen(
            ["djvu2pdf", str(safe_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, err = p.communicate()
        if p.returncode == 0:
            print('Processing finished')
            exit('Completed successfully')
        else:
            print(f'[!] Error processing file: {err.decode() if err else "Unknown error"}')
            exit('Failed')
    else:
        print('No djvu file to process, running sample')
        print('Processing DJVU to PDF...')
        sample_file = Path("assets/example.djvu")
        if not sample_file.is_file():
            print('[!] Sample file not found')
            exit('Sample file missing')
        p = subprocess.Popen(
            ["djvu2pdf", str(sample_file)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, err = p.communicate()
        if p.returncode == 0:
            print('Processing finished')
            exit('Completed successfully')
        else:
            print(f'[!] Error: {err.decode() if err else "Unknown error"}')
            exit('Failed')


elif operationtype == '':
    exit('You hit enter without inputing anything, nice work, exiting.')

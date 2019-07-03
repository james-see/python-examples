# read values from a spreadsheet
import os
import fnmatch
import xlrd


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = basename
                yield filename


filename = 'assets/test.xls'
header = 1
outputfilename = ''
pathoffile = ''

workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
if header == 1:
    curr_row = 0
else:
    curr_row = -1
curr_cell = -1
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    print('Row:', curr_row)
    outputfilename = worksheet.cell_value(curr_row, 0)
    pathoffile = worksheet.cell_value(curr_row, 1)
    print('Filename: %s\nPath: %s' % (outputfilename, pathoffile))

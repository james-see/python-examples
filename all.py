"""Way to check all examples."""
import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()
print(cwd)
onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
for i in onlyfiles:
    if i.endswith('.py'):
        print(i.split('-')[0])
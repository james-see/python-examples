#!/usr/bin/python
# -*- coding: utf-8 -*-
# python arabic example
# Author: James Campbell
# Date: 2015 05 25
import codecs

exampledict = {unicode(('ا').decode('utf-8')):'ALIF',unicode(('ع').decode('utf-8')):'AYN'}
keys = exampledict.keys()
values = exampledict.values()
print(keys)
print(values)
exit()
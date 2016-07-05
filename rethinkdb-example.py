#!/usr/bin/python3
"""
Author: James Campbell
Date: July 3rd 2016
Date Updated: July 4th 2016
What: RethinkDB python example create and put data into it from pastebin site.
Documentation on RethinkDB: https://rethinkdb.com/api/python/
"""
import rethinkdb as r  # standard nomenclature 
import urllib.request
import json

url = 'http://psbdmp.com/api/dump/daily'
"""
json keys: id, data, datahash, tags, addedtime, viewed, deleted, unixtime, banned, leakedemails, 
info, total, dumped, formated, removed, textdata, spID
"""
# open example file
with open('pastedumpexample.json','rU',encoding='utf-8') as json_data:
    d = json.load(json_data)
#data = urllib.request.urlopen(url).read()	
i = 0

# list of tables to check if they exist
tables = ['hellopaste']  # you can check multiple tables here by adding more in list
r.connect('localhost', 28015).repl()
for table in tables: 
	if not r.db('test').table_list().contains(table).run(): 
		r.db('test').table_create(table).run()

for datarow in d['data']:
	#print(datarow['id'])
	r.table('hellopaste').insert({ 'id': datarow['id'],'data': datarow['data'],'datahash': datarow['datahash'], 'tags': datarow['tags'], 'addedtime': datarow['addedtime'], 'viewed': datarow['viewed'], 'deleted': datarow['deleted'], 'unixtime': datarow['unixtime'], 'banned': datarow['banned'], 'leakedemails': datarow['leakedemails'], 'info': datarow['info'], 'total':datarow['total'], 'dumped': datarow['dumped'], 'formated':datarow['formated'], 'removed':datarow['removed'], 'textdata':datarow['textdata'], 'spID':datarow['spID']}).run()
tv_shows = r.table('hellopaste').pluck('id').run()
print(tv_shows)
conn.close()
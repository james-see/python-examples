#!/usr/bin/python3
"""
Author: James Campbell
Date: July 3rd 2016
Date Updated: July 4th 2016
What: RethinkDB python example create and put data into it from pastebin site.
Documentation on RethinkDB: https://rethinkdb.com/api/python/
"""
import rethinkdb as r
import urllib.request
import urllib

urltograb = 'http://psbdmp.com/api/dump/daily'
tables = ['hellopaste']
r.connect('localhost', 28015).repl()
for table in tables: 
	if not rdb.db(self.db).table_list().contains(table).run(): 
		rdb.db(self.db).table_create(table).run()


#r.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()
tv_shows = r.table('tv_shows').pluck('name').run()
print(tv_shows)
conn.close()
#!/usr/bin/python3
"""
Author: James Campbell
Date: July 3rd 2016
Date Updated:
What: RethinkDB python example
More: https://rethinkdb.com/api/python/
"""
import rethinkdb as r
r.connect('localhost', 28015).repl()
if r.db('test').table('tv_shows')
#r.db('test').table_create('tv_shows').run()
#r.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()
tv_shows = r.table('tv_shows').pluck('name').run()
print(tv_shows)
conn.close()
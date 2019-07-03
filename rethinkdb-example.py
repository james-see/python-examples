#!/usr/bin/python3
"""
Author: James Campbell
Date: July 3rd 2016
Date Updated: July 4th 2016
What: RethinkDB python example create and put data into it from pastebin site.
Documentation on RethinkDB: https://rethinkdb.com/api/python/
"""
import rethinkdb as r  # standard nomenclature to use
import json

# for url implementation instead of json file (comment out example file open below -jc
# url = 'http://psbdmp.com/api/dump/daily'
# data = urllib.request.urlopen(url)
# d = json.loads(data.read().decode('utf-8-sig'))

"""
json keys: id, data, datahash, tags, addedtime, viewed, deleted, unixtime, banned, leakedemails,
info, total, dumped, formated, removed, textdata, spID
"""
# open example file
with open('pastedumpexample.json', 'rU', encoding='utf-8') as json_data:
    d = json.load(json_data)

i = 0

# list of tables to check if they exist
tables = ['hellopaste']  # you can check multiple tables here by adding more in list
conn = r.connect('localhost', 28015).repl()
for table in tables:
    if not r.db('test').table_list().contains(table).run(conn):
        r.db('test').table_create(table).run(conn)

for datarow in d['data']:
    try:
        ider = datarow['id']
    except Exception:
        ider = ''
    try:
        dataer = datarow['data']
    except Exception:
        dataer = ''
    try:
        datahasher = datarow['datahash']
    except Exception:
        datahasher = ''
    try:
        tagser = datarow['tags']
    except Exception:
        tagser = ''
    try:
        addedtimeer = datarow['addedtime']
    except Exception:
        addedtimeer = ''
    try:
        vieweder = datarow['viewed']
    except Exception:
        vieweder = ''
    try:
        deleteder = datarow['deleted']
    except Exception:
        deleteder = ''
    try:
        unixtimeer = datarow['unixtime']
    except Exception:
        unixtimeer = ''
    try:
        banneder = datarow['banned']
    except Exception:
        banneder = ''
    try:
        leakedemailser = datarow['leakedemails']
    except Exception:
        leakedemailser = ''
    try:
        infoer = datarow['info']
    except Exception:
        infoer = ''
    try:
        totaler = datarow['total']
    except Exception:
        totaler = ''
    try:
        dumpeder = datarow['dumped']
    except Exception:
        dumpeder = ''
    try:
        formateder = datarow['formated']
    except Exception:
        formateder = ''
    try:
        removeder = datarow['removed']
    except Exception:
        removeder = ''
    try:
        textdataer = datarow['textdata']
    except Exception:
        textdataer = ''
    try:
        spider = datarow['spID']
    except Exception:
        spider = ''
    r.table('hellopaste').insert({'id': ider,
                                  'data': dataer,
                                  'datahash': datahasher,
                                  'tags': tagser,
                                  'addedtime': addedtimeer,
                                  'viewed': vieweder,
                                  'deleted': deleteder,
                                  'unixtime': unixtimeer,
                                  'banned': banneder,
                                  'leakedemails': leakedemailser,
                                  'info': infoer,
                                  'total': totaler,
                                  'dumped': dumpeder,
                                  'formated': formateder,
                                  'removed': removeder,
                                  'textdata': textdataer,
                                  'spID': datarow['spID']}).run(conn)
# test using pluck
# tv_shows = r.table('hellopaste').pluck('id').run(conn)
# print(tv_shows)

# count total rows in table
totalrows = r.table('hellopaste').count().run()
print('total paste entries: {}'.format(totalrows))

# return back any that include emails
totalwithemails = r.table('hellopaste').count(
    lambda hellopaste: hellopaste['textdata']
    .match("[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}")).run()
print('total with emails in text of paste: {}'.format(totalwithemails))
# print each id and datetime stamp
for doc in r.table('hellopaste').run():
    print(doc['id'], doc['addedtime'])
conn.close()

import hug
import psycopg2

# don't forget to create postgres sql test database first:
# $ createdb test
# then connect to psql
# $ psql -h localhost -d test                                                           2 ↵
# psql (9.5.3)
# Type "help" for help.
# then create test user
# test=# create user test with password 'test';
# CREATE ROLE
# test=# grant all privileges on database test to test;
# GRANT
# test=#


@hug.get('/test')
def test_connect():
    try:
        conn = psycopg2.connect("dbname='test' user='test' host='localhost' password='test'")
        return ('connected successfully to db! ready for queries.')
    except:
        print ("I am unable to connect to the database")
        return ('failed to connect')
@hug.get('/checktable')
def test_write(user='test',table='testtable'):
    try:
        conn = psycopg2.connect("dbname='test' user='test' host='localhost' password='test'")
        print ('connected successfully to db! ready for queries.')
    except:
        print ("I am unable to connect to the database")
        return ('failed to connect')
    cur = conn.cursor()
    cur.execute("select exists(select relname from pg_class where relname='" + table + "')")
    exists = cur.fetchone()[0]
    print (exists)
    cur.close()
    if exists == True:
        return 'THIS TABLE EXISTS'
    else:
        return 'This Table does not exist'

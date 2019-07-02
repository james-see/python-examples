"""Example connect and run write to postgresql."""
import hug
import psycopg2
"""
# don't forget to create postgres sql t database first:
# $ createdb t
# then connect to psql
# $ psql -h localhost -d test                                                           2 ↵
# psql (9.5.3)
# Type "help" for help.
# then create test user
# t=# create user t with password 'test';
# CREATE ROLE
# t=# grant all privileges on database test to test;
# GRANT
# t=#
"""


@hug.get('/test')
def test_connect():
    """Test connection to db."""
    psycopg2.connect("dbname='t' user='t' host='localhost' password='test'")
    return ('connected successfully to db! ready for queries.')


@hug.get('/checktable')
def test_write(user='t', table='testtable'):
    """Test write to DB."""
    conn = psycopg2.connect("dbname='t' user='t' host='localhost' password='test'")
    print('connected successfully to db! ready for queries.')
    cur = conn.cursor()
    cur.execute("select exists(select relname from pg_class where relname='" + table + "')")
    exists = cur.fetchone()[0]
    print(exists)
    cur.close()
    if exists:
        return 'THIS TABLE EXISTS'
    else:
        return 'This Table does not exist'

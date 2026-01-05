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
    # Get database credentials from configs.py or environment variables
    try:
        from configs import db_name, db_user, db_host, db_password
    except ImportError:
        import os
        db_name = os.getenv('DB_NAME', 't')
        db_user = os.getenv('DB_USER', 't')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_password = os.getenv('DB_PASSWORD', '')
        if not db_password:
            return {'error': 'Database password not configured. Set DB_PASSWORD environment variable or configs.py'}
    
    psycopg2.connect(f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{db_password}'")
    return ('connected successfully to db! ready for queries.')


@hug.get('/checktable')
def test_write(user='t', table='testtable'):
    """Test write to DB."""
    # Get database credentials from configs.py or environment variables
    try:
        from configs import db_name, db_user, db_host, db_password
    except ImportError:
        import os
        db_name = os.getenv('DB_NAME', 't')
        db_user = os.getenv('DB_USER', 't')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_password = os.getenv('DB_PASSWORD', '')
        if not db_password:
            return {'error': 'Database password not configured. Set DB_PASSWORD environment variable or configs.py'}
    
    conn = psycopg2.connect(f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{db_password}'")
    print('connected successfully to db! ready for queries.')
    cur = conn.cursor()
    # Fix SQL injection vulnerability by using parameterized queries
    cur.execute("SELECT exists(SELECT relname FROM pg_class WHERE relname=%s)", (table,))
    exists = cur.fetchone()[0]
    print(exists)
    cur.close()
    conn.close()
    if exists:
        return 'THIS TABLE EXISTS'
    else:
        return 'This Table does not exist'

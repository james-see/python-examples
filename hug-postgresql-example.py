import hug
import psycopg2

try:
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print "I am unable to connect to the database"

@hug.get('/test')
def test_connect():
	

import urllib2
import sqlite3


from sys import argv
from time import sleep

def setup():
    ''' Process arguments and establish database connection '''

    if len(argv) == 4:
        script, url, db_string, interval_str = argv
        interval = int(interval_str)
    else:
        script, url, db_string = argv
        interval = 60

    return url, db_string, interval

# # Insert a row of data
# connection.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# connection.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# connection.close()

# url = "https://www.google.com/"

def check_site(url, interval):

    req = urllib2.Request(url)

    while True:

        try:
            resp = urllib2.urlopen(url, None, 2.5)
            # resp = urllib2.urlopen("http://google.com", None, 2.5)

            timestamp = resp.info()['date']
           
            status_code = resp.code

            INS_QUERY = "INSERT INTO Sitelogs VALUES (?, ?, ?)"
            print url, status_code, timestamp
            cursor.execute(INS_QUERY, (url, status_code, timestamp))
            connection.commit()

        except urllib2.HTTPError as e:
        	print "HTTPError", e.code
        
        except urllib2.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            # ...
            print "URLError: ", e

        resp.close()

        sleep(interval)

url, db_string, interval = setup()

connection = sqlite3.connect(db_string)

cursor = connection.cursor()  

check_site(url, interval)

    


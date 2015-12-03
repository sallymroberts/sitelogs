import urllib2
import sqlite3
connection = sqlite3.connect('sitelogs.db')
cursor = connection.cursor()

# # Insert a row of data
# connection.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# connection.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# connection.close()

url = "https://www.google.com/"
req = urllib2.Request(url)

try:
    resp = urllib2.urlopen(req)
    
    print "url: ", url
    print "status code: ", resp.code
    print "timestamp: ", resp.info()['date']

    timestamp = resp.info()['date']
    status_code = resp.code

    # QUERY = "INSERT INTO Melons VALUES (?, ?)"
    # cursor.execute(QUERY, (common_name, price))
    # connection.commit()

    INS_QUERY = "INSERT INTO Sitelogs VALUES (?, ?, ?)"
    cursor.execute(INS_QUERY, (url, status_code, timestamp))
    connection.commit()

except urllib2.HTTPError as e:
	print "HTTPError", e.code
    
except urllib2.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    # ...
    print "URLError: ", e

resp.close()

# import urllib2
# response = urllib2.urlopen('http://pythonforbeginners.com/')
# print response.info()
# html = response.read()
# # do something
# response.close()  # best practice to close the file


    


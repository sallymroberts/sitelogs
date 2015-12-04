# Checks website status, logs results to database 
# Runs continuously until manually cancelled (unless errors encountered)
# Input parameters:
#     url of website to be checked
#     database string of sqlite3 database to be checked (eg. "sitelogs.db")
#     optional wait interval in seconds (frequency of checking site status)

import urllib2
import sqlite3
from sys import argv
from time import sleep

def validate_parms():
    ''' Process and validate parameters '''

# Set valid parameters to True, before validating parameters
    valid_parm = True

# Validate optional timeout interval
# Set default interval to 60 

    if len(argv) == 4:
        script, url, db_string, interval_str = argv

        if interval_str.isdigit():
            interval = int(interval_str)
        else:
            print "Invalid interval: ", interval_str
            interval = None
            valid_parm = False 

    else:
        script, url, db_string = argv
        interval = 60

# Validate sqlite3 database string is valid format
    
    db_string_low = db_string.lower()

    if db_string_low[-3:] != ".db" or len(db_string) < 4:
        
        print "Invalid database string: ", db_string
        valid_parm = False

# If url contains a .jpg or .mov, prompt user to proceed/cancel
    
    url_low = url.lower()

    print "url, url.lower: ", url, url_low
    
    if ".jpg" in url_low or ".mov" in url_low:
        answer = raw_input("Url contains .jpg or .mov, enter c to cancel, y to proceed: ")
        if answer != 'y':
            print "job will be cancelled"
            valid_parm = False
    
    return valid_parm, url, db_string, interval

def check_site(url, interval):
    ''' Never-ending loop to:
        Check site at specified interval 
        Retrieve response info
        Log to Sitelogs table
        Wait for time interval

        End program if errors encountered
    '''

    req = urllib2.Request(url)

    while True:

        try:
            resp = urllib2.urlopen(url, None, 2.5)

            timestamp = resp.info()['date']
           
            status_code = resp.code

            INS_QUERY = "INSERT INTO Sitelogs VALUES (?, ?, ?)"

            print url, status_code, timestamp # Monitor progress 

            try:
                cursor.execute(INS_QUERY, (url, status_code, timestamp))
                connection.commit()
            except sqlite3.OperationalError as s:
                print "SQLite3 table error: ", db_string
                break
                

        except urllib2.HTTPError as e:
            print "HTTPError", e.code
            if e.code == 408:
                print "Timeout error"
            break
        
        except urllib2.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused, invalid url)
           
            print "URLError: ", e
            break

        resp.close()

        sleep(interval)

###############################################################################

# MAINLINE:
# Retrieve and validate parameters
# Connect to sqlite3 database
# Check site status and update database

valid_parm, url, db_string, interval = validate_parms()

if valid_parm:

    connection = sqlite3.connect(db_string)

    cursor = connection.cursor()  

    check_site(url, interval)
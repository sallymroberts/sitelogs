# Sitecheck

Sitecheck checks the status of the requested website and logs the status to the sqlite Sitelogs table.

###### Files include:

- requirements.txt: Contains requirements for creating a virtual environment to run the application
- sitelogs_db.py: Creates the sqlite3 sitelogs.db database and the Sitelogs table
- sitecheck.py: Checks the requested site and logs the status to the Sitelogs table

### Prepare to run the application:

- Create a virtual environment in a directory on a Mac OS X computer
- Retrieve the 3 files above from https://github.com/sallymroberts/sitelogs into the directory
- NOTE: I ran this application in a virtual environment created on a MacBook Air, with Python 2.7.10 and Sqlite 3.8.5 pre-installed. 
- If you do not have Python Sqlite 3.8.5 installed globally, install Sqlite globally or into the virtual environment. http://www.sqlite.org/download.html has a link to download sqlite 3.9.2 (and not 3.8.5), but the changes listed in the upgrades from 3.8.5 to this version are unlikely to affect the limited sqlite3 functionality used in this application.
- - If you do not have Python 2.7.10 installed globally, install Python 2.7.10 globally or into the virtual environment. https://www.python.org/downloads/mac-osx/ has a link to download Python 2.7.10 (the latest release of Python 2).
- Install the applications identified in the requirements.txt file with the command: $ pip install -r requirements.txt
- Create the sqlite3 sitelogs_db database and the Sitelogs table by executing the following command in the virtual environment: python sitelogs_db.py
 
### Run the application:

This application is executed from the command line and runs until manually cancelled from the command line.

###### Example command to run sitecheck.py file in virtual environment:

python sitecheck.py "https://www.google.com/" "sitelogs.db" 30

###### Generic syntax for command to run the sitecheck.py file:

python sitecheck.py url sqlite_3_database [interval] 

###### Parameters for sitecheck.py:

- url of website for which status is to be checked
- name of sqlite 3 database, the exact value required is "sitelogs.db", to access the database created by running command above: python sitelogs_db.py 
- optional: interval in seconds specifying frequency of checking website status; if not specified, defaults to 60
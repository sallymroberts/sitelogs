# Create sitelogs database and table

import sqlite3

connection = sqlite3.connect('sitelogs.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE Sitelogs
    (url VARCHAR(255),
    status_code INTEGER,
    timestamp VARCHAR(29)
    )''')

connection.commit()

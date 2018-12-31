import sqlite3

db = None
query = None

def initDB():
    try:
        db = sqlite3.connect('../database.db')
        query = connection.cursor()
        
        createTables()
    except sqlite3.Error as e:
        print('An SQLite error has occurred')
        exit()

def createTables():
    query.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INT UNSIGNED NOT NULL PRIMARY KEY,
            subject CHAR(4) NOT NULL,
            number TINYINT NOT NULL,
            desc TEXT NOT NULL,
            depends TEXT
        )
    ''')
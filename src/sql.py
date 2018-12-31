import sqlite3
import os

class SQL:
    path = os.path.dirname(os.path.realpath(__file__))

    def initDB(self):
        try:
            self.db = sqlite3.connect(self.path + '/../database.db')
            self.query = connection.cursor()

            self.createTables()
        except sqlite3.Error as e:
            self.db.close()
            print('An SQLite error has occurred')
            exit()

    def createTables():
        self.query.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INT UNSIGNED NOT NULL PRIMARY KEY,
                subject CHAR(4) NOT NULL,
                number TINYINT NOT NULL,
                desc TEXT NOT NULL,
                depends TEXT
            )
        ''')
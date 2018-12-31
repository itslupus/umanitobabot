import sqlite3

class SQL:
    def __init__():
        try:
            self.db = sqlite3.connect('../database.db')
            self.query = connection.cursor()
        except sqlite3.Error as e:
            print('An SQLite error has occurred')
            exit()

    def initDB():
        self.query.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INT UNSIGNED NOT NULL PRIMARY KEY,
                subject CHAR(4) NOT NULL,
                number TINYINT NOT NULL,
                desc TEXT NOT NULL,
                depends TEXT
            )
        ''')
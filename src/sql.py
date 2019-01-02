import sqlite3
import os

class SQL:
    path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        try:
            self.db = sqlite3.connect(self.path + '/../database.db')
            self.query = self.db.cursor()

            self.createTables()
        except sqlite3.Error as e:
            self.db.close()
            print('An SQLite error has occurred')
            exit()

    def createTables(self):
        self.query.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INT UNSIGNED NOT NULL PRIMARY KEY,
                subject CHAR(4) NOT NULL,
                number TINYINT NOT NULL,
                title TEXT NOT NULL,
                desc TEXT NOT NULL,
                depends TEXT
            )
        ''')
        self.db.commit()

    def getCourseInfo(self, subject, number):
        info = (subject, number)
        self.query.execute('SELECT * FROM courses WHERE subject = ? AND number = ? LIMIT 1', info)
        return self.query.fetchone()

    def updateCourseInfo(self, subject, number, desc, depends, isNew):
        return None
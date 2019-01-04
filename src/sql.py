import sqlite3
import os
import time

class SQL:
    path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        try:
            self.db = sqlite3.connect(self.path + '/../database.db')
            self.db.row_factory = sqlite3.Row
            self.query = self.db.cursor()

            self.createTables()
        except sqlite3.Error as e:
            self.db.close()
            print(e)
            print('An SQLite error has occurred')
            exit()

    def createTables(self):
        self.query.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject CHAR(4) NOT NULL,
                number TINYINT NOT NULL,
                title TEXT NOT NULL,
                desc TEXT NOT NULL,
                not_held TEXT,
                prereq TEXT,
                last_update DATE NOT NULL
            )
        ''')
        self.db.commit()

    def getCourseInfo(self, subject, number):
        self.query.execute('SELECT * FROM courses WHERE subject = ? AND number = ? LIMIT 1', (subject, number))
        return self.query.fetchone()

    def insertCourseInfo(self, subject, number, title, desc, not_held, prereq):
        self.query.execute('''
            INSERT INTO courses (subject, number, title, desc, not_held, prereq, last_update)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (subject, number, title, desc, not_held, prereq, time.time()))
        self.db.commit()

    def updateCourseInfo(self, id, title, desc, not_held, prereq):
        self.query.execute('''
            UPDATE courses
            SET title = ?, desc = ?, not_held = ?, prereq = ?, last_update = ?
            WHERE id = ?
        ''', (title, desc, not_held, prereq, time.time(), id))
        self.db.commit()
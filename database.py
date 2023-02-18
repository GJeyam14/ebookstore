import sqlite3

"""
Create Database class. 
Constructor creates connection and cursor object. 
Define methods to carry out sqlite3 functions.
"""


class Database:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

    def execute(self, query_string, parameters=None):
        if parameters:
            return self.cursor.execute(query_string, parameters)
        else:
            return self.cursor.execute(query_string)

    def executemany(self, query_string, parameters):
        return self.cursor.executemany(query_string, parameters)

    def create_table(self):
        query_string = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)"
        return self.cursor.execute(query_string)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        return self.conn.commit()

    def close_connection(self):
        return self.conn.close()

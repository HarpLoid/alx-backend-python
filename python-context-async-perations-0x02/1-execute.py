#!/usr/python3

import sqlite3

class ExecuteQuery:
    def __init__(self, connection, query, params):
        self.connection = connection
        self.query = query
        self.params = params
    
    def __enter__(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()
    
    def __exit__(self, type, value, traceback):
        self.connection.close()

connection = sqlite3.connect('users.db')
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(connection, query, params) as results:
    print(results)

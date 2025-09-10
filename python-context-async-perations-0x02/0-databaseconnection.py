#!/usr/bin/python3
import sqlite3

class DatabaseConnection:
    
    def __init__(self, connection):
        self.connection = connection
    
    def __enter__(self):
        return self.connection
    
    def __exit__(self, type, value, traceback):
        self.connection.close()

connection = sqlite3.connect('users.db')
        
with DatabaseConnection(connection) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
        
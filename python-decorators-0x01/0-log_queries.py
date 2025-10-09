import sqlite3
import functools
from datetime import datetime

#### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper_log_queries(query):
        print(f"[{datetime.now()}] Executing: {query}")
        try:
            return func(query)
        except Exception as e:
            print(f"[{datetime.now()}] Error: {e}")
            raise
    return wrapper_log_queries

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
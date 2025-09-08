import time
import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_with_db_connection():
        conn = sqlite3.connect('users.db') 
        try: 
            result = func(conn)
            return result 
        finally: 
            conn.close() 

    return wrapper_with_db_connection

def retry_on_failure(retries, delay):
    def decorator_retry_on_failure(func):
        @functools.wraps(func)
        def wrapper_retry_on_failure(conn):
            attempts = retries
            while attempts:
                try:
                    return func(conn)
                except Exception as e:
                    attempts -= 1
                    if attempts == 0:
                        raise e
                    time.sleep(delay)
        return wrapper_retry_on_failure
    return decorator_retry_on_failure
            

@with_db_connection
@retry_on_failure(retries=3, delay=2)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
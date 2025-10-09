import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_with_db_connection(user_id, new_email):
        conn = sqlite3.connect('users.db') 
        try: 
            result = func(conn, user_id, new_email)
            return result 
        finally: 
            conn.close() 

    return wrapper_with_db_connection

def transactional(func): 
    @functools.wraps(func)
    def wrapper_transactional(conn, user_id, new_email):
        try: 
            func(conn, user_id, new_email) 
            conn.commit() 
            return 
        except: 
            conn.rollback() 
            raise 

    return wrapper_transactional

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email):
    print(user_id, new_email)
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')

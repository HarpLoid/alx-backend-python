#!/usr/bin/python3

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def stream_users():
    """Streams users from database

    Keyword arguments: none
    Return: yields a user row
    """
    
    connection = mysql.connector.connect(
        host= "localhost",
        user= os.getenv("DBUSER"),
        password= os.getenv("DBPASS"),
        database= "ALX_prodev"
    )
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
    connection.close()

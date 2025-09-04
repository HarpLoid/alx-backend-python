#!/usr/bin/python3

import mysql.connector


def stream_users():
    """Streams users from database

    Keyword arguments: none
    Return: yields a user row
    """
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="H07a12r94p",
        database="ALX_prodev"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
    connection.close()

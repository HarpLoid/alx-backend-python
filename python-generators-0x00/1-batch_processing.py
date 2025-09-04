#!/usr/bin/python3

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def stream_users_in_batches(batch_size):
    """Fetches user data in batches

    Keyword arguments: batch_size
    batch_size -- size of batch fetched
    Return: yield generator object
    """

    connection = mysql.connector.connect(
        host= "localhost",
        user= os.getenv("DBUSER"),
        password= os.getenv("DBPASS"),
        database= "ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break

        yield batch
    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch of data to
    filter users over the age of 25

    Keyword arguments:batch_size
    batch_size -- size of batch
    Return: return_description
    """
    
    for user_batch in stream_users_in_batches(batch_size):
        for user in user_batch:
            if user and user['age'] > 25:
                print(user)

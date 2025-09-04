#!/usr/bin/env python3

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def stream_user_ages():
    """Streams user ages from the database.

    Keyword arguments: None
    Return: generator object
    """

    connection = mysql.connector.connect(
        host=os.getenv("DBHOST", "localhost"),
        user=os.getenv("DBUSER"),
        password=os.getenv("DBPASS"),
        database=os.getenv("DATABASE", "ALX_prodev"),
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row["age"]
    cursor.close()
    connection.close()

def average_age():
    """Calculates the average age of users.
    
    Keyword arguments: None
    Return: average age
    """
    
    total_age = 0
    number_of_users = 0
    for age in stream_user_ages():
        total_age += age
        number_of_users += 1

    print(f"Average age of users: {total_age / number_of_users}")

if __name__ == "__main__":
    average_age()

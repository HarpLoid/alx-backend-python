#!/usr/bin/python3

import mysql.connector

def connect_db():
    """Connects to the mysql database server

    Keyword arguments: none
    Return: connection to the database server
    """

    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root"
    )
    
    return connection

def create_database(connection):
    """Creates the database if it doesn't exist

    Keyword arguments: connection
    connection -- connection to the database server
    Return: none
    """
    
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    """Connects to the database created on
    the database server

    Keyword arguments: none
    Return: connection to the database
    """

    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "ALX_prodev"
    )
    return connection


def create_table(connection):
    """Connects to the database server
    Creates the table if it doesn't exist

    Keyword arguments: connection
    connection -- connection to the database server
    Return: none
    """
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) NOT NULL PRIMARY KEY DEFAULT (UUID()),
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            age DECIMAL NOT NULL
        )
        """
    )
    connection.commit()
    cursor.close()


def insert_data(connection, data):
    """Inserts data in the database if it does not exist
    
    Keyword arguments: connection, data
    connection -- connection to the database server
    data -- data to be inserted in the database
    Return: none
    """

    gen = (row for row in open(data, 'r'))

    # Skip the first row which is the header
    # of the file
    next(gen)

    cursor = connection.cursor()
    for row in gen:
        name, email, age_str = row.replace('"', '').strip().split(',')
        age = float(age_str)
        values = (name, email, age)
        cursor.execute(
            """
            INSERT INTO user_data (name, email, age) VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE email = email;
            """,
            values
        )
    connection.commit()
    cursor.close()

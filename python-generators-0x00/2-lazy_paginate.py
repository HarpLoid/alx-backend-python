#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """Fetches paginated data from
    the users database using a generator
    to lazily load each page

    Keyword arguments:page_size
    page_size -- size of data to fetch per page
    Return: generator object
    """

    offset = 0
    while True:
        if page_size < 1:
            raise ValueError("page_size must be greater than 0")
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        yield rows
        offset += page_size

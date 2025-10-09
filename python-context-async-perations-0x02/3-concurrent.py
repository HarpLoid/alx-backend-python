#!/usr/env/python3

import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db_connection:
        async with db_connection.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users

async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db_connection:
        async with db_connection.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            users = await cursor.fetchall()
            return users

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All Users:", users)
    print("Users older than 40:", older_users)

asyncio.run(fetch_concurrently())

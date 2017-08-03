#!/usr/bin/env python3

import os

import asyncio
from aiomysql import create_pool

MYSQL_HOST = 'signdata.lab.tmp.br'
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']


loop = asyncio.get_event_loop()

async def go():
    async with create_pool(host=MYSQL_HOST, port=3306,
                           user=MYSQL_USER, password=MYSQL_PASS,
                           db='mysql', loop=loop) as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 42;")
                value = await cur.fetchone()
                print(value)


loop.run_until_complete(go())

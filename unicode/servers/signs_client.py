#!/usr/bin/env python3

import sys

import asyncio
import aiohttp

BASE_URL = 'http://localhost:8000/'


async def get_chars(client, word):
    url = '{}index/{}'.format(BASE_URL, word)
    async with client.get(url) as resp:
        assert resp.status == 200
        text = await resp.text()
        _, chars = text.split('\n', 1)
        return set(chars.split())


async def get_name(client, char, semaphore):
    async with semaphore:
        url = '{}name/U+{:04X}'.format(BASE_URL, ord(char))
        async with client.get(url) as resp:
            assert resp.status == 200
            return await resp.text()


async def query(loop, words):
    async with aiohttp.ClientSession(loop=loop) as client:
        to_do = [get_chars(client, word) for word in words]
        res = await asyncio.gather(*to_do)
        chars = set.intersection(*res)
        semaphore = asyncio.Semaphore(2)
        to_do = [get_name(client, char, semaphore) for char in chars]
        names = await asyncio.gather(*to_do)
    return names


def main(args):
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(query(loop, args))
    for line in sorted(res):
        print(line)

    loop.close()


if __name__ == '__main__':
    main(sys.argv[1:])

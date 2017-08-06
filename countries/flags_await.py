#!/usr/bin/env python3

"""Download flags of top 20 countries by population

asyncio await + aiottp version

Sample run::

    $ python3 flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s

"""

import asyncio

import aiohttp  # <1>

from flags import BASE_URL, save_flag, show, main  # <2>


async def get_flag(client, cc):  # <3>
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with client.get(url) as resp:  # <4>
        assert resp.status == 200
        return await resp.read()  # <5>


async def download_one(client, cc):  # <6>
    image = await get_flag(client, cc)  # <7>
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


async def download_many(loop, cc_list):
    async with aiohttp.ClientSession(loop=loop) as client:  # <8>
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]  # <9>
        res = await asyncio.gather(*to_do)
    return len(res)  # <10>


def start(cc_list):
    loop = asyncio.get_event_loop()  # <11>
    res = loop.run_until_complete(download_many(loop, cc_list))  # <12>
    loop.close()  # <13>
    return res


if __name__ == '__main__':
    main(start)
# END FLAGS_ASYNCIO

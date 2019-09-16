#!/usr/bin/env python3

"""
Download Shanghai maps from http://media.lonelyplanet.com/ebookmaps/
"""

from concurrent import futures
from urllib import request, error
import os


BASE_URL = 'https://media.lonelyplanet.com/ebookmaps/Shanghai/'
LOCAL_DIR = 'files/'
FILE_DATA = '''
bund-overview.pdf (793 KB)
bund-wt.pdf (374 KB)
bund.pdf (1954 KB)
century-ave.pdf (984 KB)
city-overview.pdf (1928 KB)
contents.pdf (233 KB)
country-city-review-legend-asia-2C.pdf (455 KB)
day-trips-loc.pdf (257 KB)
french-east.pdf (1513 KB)
french-overview.pdf (656 KB)
french-west.pdf (1464 KB)
french-wt.pdf (342 KB)
hangzhou.pdf (2140 KB)
hongkou-overview.pdf (768 KB)
hongkou.pdf (2620 KB)
jingan-overview.pdf (722 KB)
jingan-wt.pdf (299 KB)
north-jingan.pdf (1208 KB)
old-town-overview.pdf (653 KB)
old-town-wt.pdf (352 KB)
old-town.pdf (2149 KB)
pudong-overview.pdf (554 KB)
pudong-wt.pdf (395 KB)
pudong.pdf (1332 KB)
shanghai-index.pdf (1594 KB)
south-jingan.pdf (2254 KB)
suzhou.pdf (1771 KB)
west-shanghai-overview.pdf (971 KB)
west-shanghai.pdf (3240 KB)
xujiahui-overview.pdf (454 KB)
xujiahui.pdf (1883 KB)
'''


def names():
    for line in FILE_DATA.strip().split('\n'):
        yield line.split()[0]


def get_file(name, timeout):
    """Download ans save a single file"""

    url = BASE_URL + name

    with request.urlopen(url, timeout=timeout) as conn:
        data = conn.read()

    with open(LOCAL_DIR + name, 'wb') as fp:
        fp.write(data)

    return (name, len(data))



def main():
    with futures.ThreadPoolExecutor() as executor:

        downloads = [executor.submit(get_file, name, 60)
                        for name in names()]

        for future in futures.as_completed(downloads):
            try:
                name, length = future.result()
            except error.HTTPError as exc:
                print(f'*** {exc} ({exc.url})')
            else:
                print(f'{length:9,d} bytes\t{name}')


main()

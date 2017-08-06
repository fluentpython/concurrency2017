#!/usr/bin/env python3

"""Download flags of top 20 countries by population

ThreadPoolExecutor version 2, with ``as_completed``.

Sample run::

    $ python3 flags_threadpool_ac.py
    Scheduled for BR: <Future at 0x7fdf10e8e7b8 state=running>
    Scheduled for CN: <Future at 0x7fdf1061a278 state=running>
    Scheduled for ID: <Future at 0x7fdf1061a828 state=running>
    Scheduled for IN: <Future at 0x7fdf1061ada0 state=pending>
    Scheduled for US: <Future at 0x7fdf1061ae48 state=pending>
    ID <Future at 0x7fdf1061a828 state=finished returned str> result: 'ID'
    BR CN <Future at 0x7fdf10e8e7b8 state=finished returned str> result: 'BR'
    <Future at 0x7fdf1061a278 state=finished returned str> result: 'CN'
    US <Future at 0x7fdf1061ae48 state=finished returned str> result: 'US'
    IN <Future at 0x7fdf1061ada0 state=finished returned str> result: 'IN'

    5 flags downloaded in 0.61s

"""
from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    cc_list = cc_list[:5]  # <1>
    with futures.ThreadPoolExecutor(max_workers=3) as executor:  # <2>
        to_do = []
        for cc in sorted(cc_list):  # <3>
            future = executor.submit(download_one, cc)  # <4>
            to_do.append(future)  # <5>
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))  # <6>

        results = []
        for future in futures.as_completed(to_do):  # <7>
            res = future.result()  # <8>
            msg = '{} result: {!r}'
            print(msg.format(future, res))  # <9>
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)

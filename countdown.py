#!/usr/bin/env python3

# Inspired by
# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

"""
A key lesson of this example is that an `async` function which never does
`await` is really synchronous. The `async/await` keywords enable cooperative
multitasking, but that only works if you use `await` to allow the event loop
schedule other tasks concurrently.

To see this working, run this script with an `s` argument, like this::

    $ ./countdown s

This will use a regular `time.sleep(s)` call instead of `await asyncio.sleep(s)`.
Run the program with and without the `s` option to see the effect.
"""


import asyncio
import time
import sys

async def countdown(label, n, delay):
    tabs = (ord(label) - ord('A')) * '\t'
    while n > 0:
        if async_delay:  # make this function asynchronous
            await asyncio.sleep(delay)
        else:  # make this function synchronous
            time.sleep(delay)
        dt = time.perf_counter() - t0
        print('{:0.4f}s \t{}{} = {}'.format(dt, tabs, label, n))
        n -= 1


if len(sys.argv) > 1 and sys.argv[1] == 's':
    async_delay = False
else:
    async_delay = True

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(countdown('A', 3, .7)),
    loop.create_task(countdown('B', 2, 2)),
    loop.create_task(countdown('C', 3, .3)),
    loop.create_task(countdown('D', 3, 1)),
]
t0 = time.perf_counter()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

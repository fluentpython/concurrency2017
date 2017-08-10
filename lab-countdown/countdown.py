#!/usr/bin/env python3

# Inspired by
# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

"""
The `async/await` keywords enable cooperative multitasking, but that only
works when functions *cooperate* by using `await` to let the scheduler run
other tasks concurrently.

As an experiment, replace the line labeled `<A>` with this::

    time.sleep(delay)

Save and run the program to see the effect. Discuss with your neighboors and
with the instructor.

A key lesson of this example is that an `async` function which never does
`await` is really synchronous.
"""


import asyncio
import time


async def countdown(label, delay):
    tabs = (ord(label) - ord('A')) * '\t'
    n = 3
    while n > 0:
        await asyncio.sleep(delay)  # <---- <A>
        dt = time.perf_counter() - t0
        print('{:7.4f}s \t{}{} = {}'.format(dt, tabs, label, n))
        n -= 1

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(countdown('A', .7)),
    loop.create_task(countdown('B', 2)),
    loop.create_task(countdown('C', .3)),
    loop.create_task(countdown('D', 1)),
]
t0 = time.perf_counter()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

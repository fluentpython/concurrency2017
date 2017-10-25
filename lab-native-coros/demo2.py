#!/usr/bin/env python3

# A slightly more interesting demo
# Now the generator-coroutine yields 3 times.

import types


@types.coroutine
def gen123():
    yield 1
    yield 2
    yield 3


async def delegating():
    await gen123()


# Driving code:
coro = delegating()
res = coro.send(None)
print(res)

res = coro.send(None)
print(res)

res = coro.send(None)
print(res)

coro.send(None)  # --> StopIteration

# coro.send(None)  # --> RuntimeError

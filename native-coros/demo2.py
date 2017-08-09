#!/usr/bin/env python3

# A slightly more interesting demo
# Now the generator-coroutine yields 3 times.

import types


@types.coroutine
def gen123():
    return (i for i in range(1, 4))


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

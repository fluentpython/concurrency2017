#!/usr/bin/env python3

# The simplest native coroutine demo
# (that I could imagine)

import types


@types.coroutine
def gen():
    yield 42


async def delegating():
    await gen()


# The driving code starts here:
coro = delegating()

res = coro.send(None)
print(res)

res = coro.send(None)
print(res)  # Never executed. Why?

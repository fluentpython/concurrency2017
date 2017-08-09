#!/usr/bin/env python3

# A generator-coroutine that receives values
# The driving code can send values other than `None`.

import types


@types.coroutine
def times10(terms):
    n = yield 'Primed!'
    for _ in range(terms):
        n = yield n * 10
    return n * 10


async def delegating(terms):
    res = await times10(terms)
    return res

# Driving code must *prime* the coroutine by sending `None` initially:

coro = delegating(3)
res = coro.send(None)
print('send(None):', res)

res = coro.send(5)
print('send(5):', res)

res = coro.send(6)
print('send(6):', res)

res = coro.send(7)
print('send(7):', res)

try:
    coro.send(8)
except StopIteration as e:
    res = e.value
print('send(8):', res)

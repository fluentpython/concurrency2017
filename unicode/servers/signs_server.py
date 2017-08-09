#!/usr/bin/env python3

import time
import unicodedata
import asyncio
import sys

from aiohttp import web
import click

from signs import build_index

PORT = 8000


async def usage(request):
    text = (
        'use\t/index/«word» to get list of characters '
        'with «word» in their Unicode names\n'
        '\t/name/«c» to get Unicode name of character «c»'
    )
    return web.Response(text=text)


async def index_for(request):
    print('!' if semaphore.locked() else '.', end='')
    sys.stdout.flush()
    async with semaphore:
        word = request.match_info.get('word', '')
        chars = index.get(word.upper(), [])
        text = f'{len(chars)} found\n'
        if chars:
            text += ' '.join(chars)
        if global_sleep:
            time.sleep(global_sleep)
        if local_sleep:
            await asyncio.sleep(local_sleep)

        return web.Response(text=text)


def parse_codepoint(codepoint):
    codepoint = codepoint.replace('U+', '')
    try:
        return chr(int(codepoint, 16))
    except ValueError:
        raise web.HTTPBadRequest(
            text='Invalid hex number after U+ codepoint prefix.')


async def char_name(request):
    char = request.match_info.get('char', '')
    if char.upper().startswith('U+'):
        char = parse_codepoint(char)
    if len(char) > 1:
        raise web.HTTPBadRequest(
            text='Only one character per request is allowed.')
    name = unicodedata.name(char, None)
    codepoint = 'U+{:04X}'.format(ord(char))
    if name is None:
        raise web.HTTPNotFound(text=
            'No name for character {} in Unicode 9.'.format(codepoint))
    text = '\t'.join([codepoint, name, char])
    return web.Response(text=text)


@click.command()
@click.option('-g', 'global_delay', default=0.0)
@click.option('-l', 'local_delay', default=0.0)
@click.option('-c', 'concurrency', default=sys.maxsize)
def main(global_delay, local_delay, concurrency):
    global global_sleep, local_sleep, semaphore, index
    global_sleep = global_delay
    local_sleep = local_delay
    semaphore = asyncio.Semaphore(concurrency)
    print('Global delay =', global_delay)
    print('Local delay =', local_delay)
    print('Max. concurrency =', concurrency)
    print('Building inverted index...')
    index = build_index()

    app = web.Application()
    app.router.add_get('/', usage)
    app.router.add_get('/index/{word}', index_for)
    app.router.add_get('/name/{char}', char_name)

    print('Listening on port', PORT)
    web.run_app(app, port=PORT)


if __name__ == '__main__':
    main()

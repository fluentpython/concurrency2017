#!/usr/bin/env python3

from aiohttp import web

from signs import build_index

import unicodedata

PORT = 8000

async def usage(request):
    return web.Response(text='use /<word> to get list of characters '
                             'with <word> in their Unicode names')


async def index_for(request):
    word = request.match_info.get('word', '')
    chars = index.get(word.upper(), [])
    text = f'{len(chars)} found\n'
    if chars:
        text += ' '.join(chars)
    return web.Response(text=text)

async def char_name(request):
    char = request.match_info.get('char', '')

    name = unicodedata.name(char, None)
    if name is None:
        raise(HTTPNotFound('No name for character {} in Unicode 9.'.format(char)))
    text = f'U+{ord(char):04x}\t{char}\t{name}'
    return web.Response(text=text)


if __name__ == '__main__':
    print('Building inverted index...')
    index = build_index()

    app = web.Application()
    app.router.add_get('/', usage)
    app.router.add_get('/index/{word}', index_for)
    app.router.add_get('/char/{char}', char_name)

    print('Listening on port', PORT)
    web.run_app(app, port=PORT)

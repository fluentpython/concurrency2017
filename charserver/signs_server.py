#!/usr/bin/env python3

from aiohttp import web

from signs import build_index


async def usage(request):
    return web.Response(text='use /<word> to get list of characters '
                             'with <word> in their Unicode names')


async def handle(request):
    word = request.match_info.get('word', '')
    chars = index.get(word.upper(), [])
    text = f'{len(chars)} found\n'
    if chars:
        text += ' '.join(chars)
    return web.Response(text=text)


if __name__ == '__main__':
    index = build_index()

    app = web.Application()
    app.router.add_get('/', usage)
    app.router.add_get('/{word}', handle)

    web.run_app(app, port=8000)

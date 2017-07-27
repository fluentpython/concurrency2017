#!/usr/bin/env python3

import sys
import unicodedata


def named_chars():
    for code in range(sys.maxunicode):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name is not None:
            yield char, name


def build_index(char_names=None):
    index = {}
    if char_names is None:
        char_names = named_chars()
    for char, name in char_names:
        words = name.replace('-', ' ').split()
        for word in words:
            index.setdefault(word, []).append(char)
    return index


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('use word.py <word> to get list of characters '
              'with <word> in their Unicode names')
        sys.exit(1)

    index = build_index(named_chars())

    chars = index.get(sys.argv[1].upper(), [])
    print('found', len(chars))
    if chars:
        print(' '.join(chars))

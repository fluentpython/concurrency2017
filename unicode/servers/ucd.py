"""UCD: Unicode Data parser"""

from collections import namedtuple

NameRecord = namedtuple('NameRecord', 'code name old_name words')

UCD_FILE_NAME = 'UnicodeData.txt'


def parse_line(line):
    fields = line.split(';')
    code = int(fields[0], 16)
    name = fields[1]
    old_name = fields[10]
    words = set(name.replace('-', ' ').split())
    if old_name:
        words.update(old_name.replace('-', ' ').split())
    return NameRecord(code, name, old_name, sorted(words))


def parser():
    with open(UCD_FILE_NAME) as ucd:
        for line in ucd:
            record = parse_line(line)
            if record.name.startswith('<'):  # not a printable character
                continue
            yield record


def index(records):
    inverted_idx = {}
    for record in records:
        for word in record.words:
            inverted_idx.setdefault(word, []).append(record.code)
    return inverted_idx

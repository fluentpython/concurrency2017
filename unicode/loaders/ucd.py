"""UCD: Unicode Data parser"""

UCD_FILE_NAME = 'UnicodeData.txt'


def parse_line(line):
    fields = line.split(';')
    code = int(fields[0], 16)
    name = fields[1]
    old_name = fields[10]
    words = set(name.replace('-', ' ').split())
    if old_name:
        words.update(old_name.replace('-', ' ').split())
    return code, name, old_name, sorted(words)


def parser():
    with open(UCD_FILE_NAME) as ucd:
        for line in ucd:
            code, name, *rest = parse_line(line)
            if name.startswith('<'):  # not a printable character
                continue
            yield (code, name) + tuple(rest)

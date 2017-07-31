import itertools

import ucd

ABC_LINES = '''
0040;COMMERCIAL AT;Po;0;ON;;;;;N;;;;;
0041;LATIN CAPITAL LETTER A;Lu;0;L;;;;;N;;;;0061;
0042;LATIN CAPITAL LETTER B;Lu;0;L;;;;;N;;;;0062;
0043;LATIN CAPITAL LETTER C;Lu;0;L;;;;;N;;;;0063;
'''.strip()


def test_parse_line():
    line_A = '0041;LATIN CAPITAL LETTER A;Lu;0;L;;;;;N;;;;0061;'
    code, name, old_name, words = ucd.parse_line(line_A)
    assert code == 65
    assert name == 'LATIN CAPITAL LETTER A'
    assert old_name == ''
    assert words == ['A', 'CAPITAL', 'LATIN', 'LETTER']


def test_parse_line_with_hyphen_and_field_10():
    cases = [
        ('002D;HYPHEN-MINUS;Pd;0;ES;;;;;N;;;;;',
         45, 'HYPHEN-MINUS', '', ['HYPHEN', 'MINUS']),
        ('005F;LOW LINE;Pc;0;ON;;;;;N;SPACING UNDERSCORE;;;;',
         95, 'LOW LINE', 'SPACING UNDERSCORE',
            ['LINE', 'LOW', 'SPACING', 'UNDERSCORE']),
        ('0027;APOSTROPHE;Po;0;ON;;;;;N;APOSTROPHE-QUOTE;;;',
         39, 'APOSTROPHE', 'APOSTROPHE-QUOTE', ['APOSTROPHE', 'QUOTE']),
    ]

    for line, *fields_ok in cases:
        fields = ucd.parse_line(line)
        assert fields == tuple(fields_ok)


def test_parser_top_3():
    records = list(itertools.islice(ucd.parser(), 3))
    assert records == [
            (32, 'SPACE', '', ['SPACE']),
            (33, 'EXCLAMATION MARK', '', ['EXCLAMATION', 'MARK']),
            (34, 'QUOTATION MARK', '', ['MARK', 'QUOTATION']),
    ]


def test_index():
    line = '003E;GREATER-THAN SIGN;Sm;0;ON;;;;;Y;;;;;'
    record = ucd.parse_line(line)
    idx = ucd.index([record])
    assert idx == {'GREATER': [62], 'SIGN': [62], 'THAN': [62]}


def test_index_abc():
    records = [ucd.parse_line(line) for line in ABC_LINES.split('\n')]
    idx = ucd.index(records)
    assert idx == {
        'A': [65],
        'AT': [64],
        'B': [66],
        'C': [67],
        'CAPITAL': [65, 66, 67],
        'COMMERCIAL': [64],
        'LATIN': [65, 66, 67],
        'LETTER': [65, 66, 67],
    }

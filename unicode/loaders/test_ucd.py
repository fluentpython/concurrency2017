import itertools

import ucd


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

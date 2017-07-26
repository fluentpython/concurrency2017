import pytest
import itertools

from word import named_chars, build_index

@pytest.fixture
def first_5():
    return [(' ', 'SPACE'),
            ('!', 'EXCLAMATION MARK'),
            ('"', 'QUOTATION MARK'),
            ('#', 'NUMBER SIGN'),
            ('$', 'DOLLAR SIGN')]


def test_first_5_named(first_5):
    assert first_5 == list(itertools.islice(named_chars(), 5))


def test_build_index(first_5):
    index = build_index(first_5)
    assert len(index) == 7
    assert index['SPACE'] == [' ']
    assert index['EXCLAMATION'] == ['!']
    assert index['SIGN'] == ['#', '$']

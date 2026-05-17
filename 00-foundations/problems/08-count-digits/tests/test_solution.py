import pytest

from solution import count_digits


@pytest.mark.parametrize("n, expected", [(0, 1), (7, 1), (42, 2), (12345, 5), (10**6, 7), (10**100, 101)])
def test_examples(n, expected):
    assert count_digits(n) == expected


def test_matches_str_len():
    for n in (0, 1, 9, 10, 99, 100, 999, 1_234_567):
        assert count_digits(n) == len(str(n))


def test_negative_raises():
    with pytest.raises(ValueError):
        count_digits(-7)

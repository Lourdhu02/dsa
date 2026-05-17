import pytest

from solution import popcount


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (7, 3), (11, 3), (255, 8), (2**31 - 1, 31)])
def test_examples(n, expected):
    assert popcount(n) == expected


def test_matches_stdlib():
    for n in (0, 1, 7, 11, 256, 2**20 - 1, 2**32 - 1):
        assert popcount(n) == n.bit_count()


def test_negative_raises():
    with pytest.raises(ValueError):
        popcount(-1)

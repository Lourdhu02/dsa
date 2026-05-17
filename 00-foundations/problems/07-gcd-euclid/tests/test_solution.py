import math

import pytest

from solution import gcd


@pytest.mark.parametrize(
    "a, b, expected",
    [(48, 18, 6), (0, 7, 7), (7, 0, 7), (1071, 462, 21), (17, 13, 1), (1, 1, 1)],
)
def test_small(a, b, expected):
    assert gcd(a, b) == expected


def test_matches_stdlib():
    for a in (0, 1, 6, 36, 999_983):
        for b in (0, 1, 2, 5, 18, 21, 999_983):
            assert gcd(a, b) == math.gcd(a, b)


def test_negative_raises():
    with pytest.raises(ValueError):
        gcd(-1, 5)

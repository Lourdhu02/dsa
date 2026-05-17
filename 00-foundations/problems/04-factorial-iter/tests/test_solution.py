import math

import pytest

from solution import factorial


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (10, 3_628_800), (12, 479_001_600)])
def test_small(n, expected):
    assert factorial(n) == expected


def test_matches_stdlib():
    for n in range(20):
        assert factorial(n) == math.factorial(n)


def test_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)

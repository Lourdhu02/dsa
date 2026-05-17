import math

import pytest

from solution import trailing_zeros


@pytest.mark.parametrize(
    "n, expected", [(0, 0), (4, 0), (5, 1), (10, 2), (25, 6), (100, 24), (1000, 249), (10**9, 249_999_998)]
)
def test_examples(n, expected):
    assert trailing_zeros(n) == expected


def test_agrees_with_brute_force_for_small_n():
    for n in range(50):
        s = str(math.factorial(n))
        expected = len(s) - len(s.rstrip("0"))
        assert trailing_zeros(n) == expected

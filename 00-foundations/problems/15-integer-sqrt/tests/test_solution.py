import math

import pytest

from solution import isqrt


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (1, 1), (4, 2), (8, 2), (16, 4), (99, 9), (10**18, 10**9)],
)
def test_examples(n, expected):
    assert isqrt(n) == expected


def test_matches_stdlib():
    for n in (0, 1, 2, 3, 4, 5, 100, 12345, 2**40, 2**63 - 1):
        assert isqrt(n) == math.isqrt(n)


def test_invariant_holds():
    for n in (0, 1, 8, 99, 10_000, 10**12):
        r = isqrt(n)
        assert r * r <= n
        assert (r + 1) * (r + 1) > n

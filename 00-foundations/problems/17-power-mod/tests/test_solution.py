import random

import pytest

from solution import pow_mod


@pytest.mark.parametrize(
    "a, n, m, expected",
    [(2, 10, 1000, 24), (5, 0, 7, 1), (3, 200, 13, 9), (7, 1_000_000, 19, 1), (10, 5, 1, 0)],
)
def test_examples(a, n, m, expected):
    assert pow_mod(a, n, m) == expected


def test_matches_builtin_pow():
    rng = random.Random(123)
    for _ in range(200):
        a = rng.randint(0, 10_000)
        n = rng.randint(0, 10_000)
        m = rng.randint(1, 10_000)
        assert pow_mod(a, n, m) == pow(a, n, m)

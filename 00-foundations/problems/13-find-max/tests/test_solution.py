import random

import pytest

from solution import find_max


@pytest.mark.parametrize(
    "xs, expected",
    [([3], 3), ([-1, -2, -3], -1), ([5, 1, 5, 1], 5), ([1, 2, 3, 4, 5], 5), ([0, 0, 0], 0)],
)
def test_examples(xs, expected):
    assert find_max(xs) == expected


def test_random_matches_builtin():
    rng = random.Random(42)
    for _ in range(100):
        xs = [rng.randint(-100, 100) for _ in range(rng.randint(1, 200))]
        assert find_max(xs) == max(xs)


def test_empty_raises():
    with pytest.raises(ValueError):
        find_max([])

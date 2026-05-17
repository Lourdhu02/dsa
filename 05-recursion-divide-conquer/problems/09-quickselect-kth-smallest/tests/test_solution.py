import random
import pytest

from solution import kth_smallest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 3),
        ([1], 1, 1),
    ],
)
def test_examples(nums, k, expected):
    assert kth_smallest(nums, k) == expected


def test_random_matches_sorted():
    rng = random.Random(42)
    for _ in range(20):
        n = rng.randint(1, 100)
        xs = [rng.randint(-100, 100) for _ in range(n)]
        s = sorted(xs)
        for k in (1, n // 2 + 1, n):
            assert kth_smallest(xs, k) == s[k - 1]

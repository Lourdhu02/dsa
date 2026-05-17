import random

from solution import quick_sort


def test_matches_sorted():
    rng = random.Random(1)
    for _ in range(10):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        assert quick_sort(xs[:]) == sorted(xs)

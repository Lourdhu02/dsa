import pytest
import random
from solution import heap_sort


def test_basic():
    a = [3, 1, 4, 1, 5, 9, 2, 6]
    heap_sort(a)
    assert a == sorted([3, 1, 4, 1, 5, 9, 2, 6])


def test_random():
    rng = random.Random(0)
    for _ in range(10):
        a = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        expected = sorted(a)
        heap_sort(a)
        assert a == expected

import pytest
from solution import smallest_range


def test_basic():
    assert smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]


def test_singletons():
    assert smallest_range([[1], [2], [3]]) == [1, 3]

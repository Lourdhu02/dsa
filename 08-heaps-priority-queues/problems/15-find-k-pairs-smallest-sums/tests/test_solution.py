import pytest
from solution import k_smallest_pairs


def test_basic():
    res = k_smallest_pairs([1, 7, 11], [2, 4, 6], 3)
    assert sorted(map(tuple, res)) == sorted([(1, 2), (1, 4), (1, 6)])


def test_k_larger_than_pairs():
    res = k_smallest_pairs([1, 2], [3], 10)
    assert sorted(map(tuple, res)) == sorted([(1, 3), (2, 3)])

import pytest
from solution import all_paths


def test_basic():
    assert sorted(all_paths([[1, 2], [3], [3], []])) == sorted([[0, 1, 3], [0, 2, 3]])


def test_one_node():
    assert all_paths([[]]) == [[0]]

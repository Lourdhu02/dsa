import pytest
from solution import num_islands


def test_one():
    g = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert num_islands(g) == 1


def test_three():
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g) == 3


def test_empty():
    assert num_islands([]) == 0

import pytest
from solution import eventual_safe_nodes


def test_basic():
    assert eventual_safe_nodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]

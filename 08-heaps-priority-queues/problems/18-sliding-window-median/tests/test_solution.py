import pytest
from solution import median_sliding_window


def test_basic():
    assert median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1, -1, -1, 3, 5, 6]


def test_window_size_1():
    assert median_sliding_window([1, 2, 3, 4], 1) == [1, 2, 3, 4]

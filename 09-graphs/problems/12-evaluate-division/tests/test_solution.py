import pytest
from solution import calc_equation


def test_basic():
    out = calc_equation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    assert out == [6.0, 0.5, -1.0, 1.0, -1.0]

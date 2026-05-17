import pytest
from solution import tsp


def test_basic():
    dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    assert tsp(dist) == 80


def test_two_cities():
    assert tsp([[0, 5], [5, 0]]) == 10

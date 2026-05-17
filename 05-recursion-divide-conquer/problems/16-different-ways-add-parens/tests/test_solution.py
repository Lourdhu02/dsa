import pytest

from solution import diff_ways_to_compute


def test_simple():
    assert sorted(diff_ways_to_compute("2-1-1")) == [0, 2]


def test_complex():
    assert sorted(diff_ways_to_compute("2*3-4*5")) == [-34, -14, -10, -10, 10]


def test_single_number():
    assert diff_ways_to_compute("17") == [17]

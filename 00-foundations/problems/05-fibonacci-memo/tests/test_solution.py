import pytest

from solution import fib


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (10, 55), (20, 6765), (30, 832040)],
)
def test_small(n, expected):
    assert fib(n) == expected


def test_recurrence():
    for n in range(2, 50):
        assert fib(n) == fib(n - 1) + fib(n - 2)


def test_large():
    # If memoization is working you can hit n=200 fast; without it this hangs.
    assert fib(100) == 354_224_848_179_261_915_075

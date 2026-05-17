import pytest

from solution import fib


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (1, 1), (2, 1), (10, 55), (50, 12586269025), (100, 354_224_848_179_261_915_075)],
)
def test_small(n, expected):
    assert fib(n) == expected


def test_recurrence():
    for n in range(2, 200):
        assert fib(n) == fib(n - 1) + fib(n - 2)


def test_negative_raises():
    with pytest.raises(ValueError):
        fib(-1)

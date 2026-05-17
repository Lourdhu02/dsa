import pytest

from solution import my_pow


@pytest.mark.parametrize(
    "x, n, expected",
    [(2.0, 10, 1024.0), (2.1, 3, 9.261), (2.0, -2, 0.25), (1.0, 1000, 1.0)],
)
def test_examples(x, n, expected):
    assert abs(my_pow(x, n) - expected) < 1e-9

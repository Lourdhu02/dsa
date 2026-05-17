import pytest

from solution import power


@pytest.mark.parametrize(
    "a, n, expected",
    [(2.0, 10, 1024.0), (2.0, -2, 0.25), (0.0, 0, 1.0), (3.0, 4, 81.0), (5.0, 1, 5.0)],
)
def test_examples(a, n, expected):
    assert abs(power(a, n) - expected) < 1e-9

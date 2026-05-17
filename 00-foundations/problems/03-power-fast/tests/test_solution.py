import pytest

from solution import power_fast, power_linear


@pytest.mark.parametrize(
    "a, n, expected",
    [(2, 10, 1024), (3, 0, 1), (5, 3, 125), (-2, 5, -32), (10, 6, 1_000_000), (1, 1_000_000, 1)],
)
def test_fast(a, n, expected):
    assert power_fast(a, n) == expected


@pytest.mark.parametrize("a, n, expected", [(2, 10, 1024), (3, 0, 1), (-3, 4, 81)])
def test_linear(a, n, expected):
    assert power_linear(a, n) == expected


def test_fast_agrees_with_python_builtin():
    # cross-check against the built-in pow.
    for a in (-3, -1, 0, 1, 2, 7):
        for n in range(20):
            assert power_fast(a, n) == pow(a, n)

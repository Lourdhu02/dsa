import pytest

from solution import sum_to_n_formula, sum_to_n_loop


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 3), (4, 10), (100, 5050), (1_000, 500_500)])
def test_loop(n, expected):
    assert sum_to_n_loop(n) == expected


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 3), (4, 10), (100, 5050), (1_000_000_000, 500_000_000_500_000_000)])
def test_formula(n, expected):
    assert sum_to_n_formula(n) == expected


def test_loop_and_formula_agree():
    for n in range(50):
        assert sum_to_n_loop(n) == sum_to_n_formula(n)

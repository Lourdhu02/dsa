import pytest
from solution import find_cheapest_price


flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]


@pytest.mark.parametrize(
    "k, expected",
    [(1, 200), (0, 500)],
)
def test_examples(k, expected):
    assert find_cheapest_price(3, flights, 0, 2, k) == expected

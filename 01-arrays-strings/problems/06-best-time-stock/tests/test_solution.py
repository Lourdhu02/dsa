import pytest

from solution import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 4, 1], 2),
        ([], 0),
        ([1, 2, 3, 4, 5], 4),
    ],
)
def test_examples(prices, expected):
    assert max_profit(prices) == expected

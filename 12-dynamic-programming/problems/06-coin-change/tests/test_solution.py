import pytest
from solution import coin_change


@pytest.mark.parametrize(
    "coins, amount, expected",
    [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([1, 4, 5], 7, 2)],
)
def test_examples(coins, amount, expected):
    assert coin_change(coins, amount) == expected

import pytest
from solution import coin_change_count


@pytest.mark.parametrize(
    "amount, coins, expected",
    [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1), (0, [], 1)],
)
def test_examples(amount, coins, expected):
    assert coin_change_count(amount, coins) == expected

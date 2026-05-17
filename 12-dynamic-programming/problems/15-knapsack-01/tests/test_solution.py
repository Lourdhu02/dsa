import pytest
from solution import knapsack


@pytest.mark.parametrize(
    "weights, values, cap, expected",
    [([2, 3, 4, 5], [3, 4, 5, 6], 5, 7), ([1, 2, 3], [6, 10, 12], 5, 22)],
)
def test_examples(weights, values, cap, expected):
    assert knapsack(weights, values, cap) == expected

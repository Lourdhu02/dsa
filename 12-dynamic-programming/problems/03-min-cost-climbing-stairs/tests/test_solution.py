import pytest
from solution import min_cost_climbing_stairs


@pytest.mark.parametrize(
    "cost, expected",
    [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)],
)
def test_examples(cost, expected):
    assert min_cost_climbing_stairs(cost) == expected

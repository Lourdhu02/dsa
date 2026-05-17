import pytest
from solution import can_complete_circuit


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5], [4], 0),
    ],
)
def test_examples(gas, cost, expected):
    assert can_complete_circuit(gas, cost) == expected

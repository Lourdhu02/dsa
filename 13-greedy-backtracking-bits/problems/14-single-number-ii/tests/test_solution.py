import pytest
from solution import single_number_ii


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 2, 3, 2], 3), ([0, 1, 0, 1, 0, 1, 99], 99), ([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], -4)],
)
def test_examples(nums, expected):
    assert single_number_ii(nums) == expected

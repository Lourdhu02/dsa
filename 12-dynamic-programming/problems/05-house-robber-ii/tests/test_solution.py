import pytest
from solution import rob_circular


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([5], 5), ([1, 2, 3], 3)],
)
def test_examples(nums, expected):
    assert rob_circular(nums) == expected

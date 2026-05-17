import pytest
from solution import can_partition


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 5, 11, 5], True), ([1, 2, 3, 5], False), ([2, 2], True), ([1], False)],
)
def test_examples(nums, expected):
    assert can_partition(nums) is expected

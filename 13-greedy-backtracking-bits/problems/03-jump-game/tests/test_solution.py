import pytest
from solution import can_jump


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), ([0], True), ([1, 0, 1], False)],
)
def test_examples(nums, expected):
    assert can_jump(nums) is expected

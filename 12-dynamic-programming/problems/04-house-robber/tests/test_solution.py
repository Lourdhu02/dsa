import pytest
from solution import rob


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12), ([], 0), ([5], 5)],
)
def test_examples(nums, expected):
    assert rob(nums) == expected

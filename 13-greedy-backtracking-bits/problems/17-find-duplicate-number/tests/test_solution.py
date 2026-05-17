import pytest
from solution import find_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3), ([1, 1], 1), ([1, 1, 2], 1)],
)
def test_examples(nums, expected):
    assert find_duplicate(nums) == expected

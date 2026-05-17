import pytest

from solution import majority_element


@pytest.mark.parametrize(
    "nums, expected",
    [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2), ([1], 1), ([1, 1, 1, 2], 1)],
)
def test_examples(nums, expected):
    assert majority_element(nums) == expected

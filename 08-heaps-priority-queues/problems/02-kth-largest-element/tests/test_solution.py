import pytest
from solution import find_kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4), ([1], 1, 1)],
)
def test_examples(nums, k, expected):
    assert find_kth_largest(nums, k) == expected

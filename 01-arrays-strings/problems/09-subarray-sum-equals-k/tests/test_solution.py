import pytest

from solution import subarray_sum


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 1, -1], 0, 4),
        ([0, 0, 0], 0, 6),
        ([1], 0, 0),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ],
)
def test_examples(nums, k, expected):
    assert subarray_sum(nums, k) == expected

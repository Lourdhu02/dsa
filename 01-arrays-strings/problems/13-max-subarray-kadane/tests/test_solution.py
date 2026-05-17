import pytest

from solution import max_subarray


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-3, -2, -1], -1),
        ([0, 0, 0], 0),
    ],
)
def test_examples(nums, expected):
    assert max_subarray(nums) == expected

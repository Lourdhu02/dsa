import pytest

from solution import two_sum


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([1, 5, 1, 5], 6, (0, 1)),
    ],
)
def test_examples(nums, target, expected):
    assert two_sum(nums, target) == expected

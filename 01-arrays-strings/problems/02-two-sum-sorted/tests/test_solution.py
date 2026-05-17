import pytest

from solution import two_sum_sorted


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, (1, 2)),
        ([2, 3, 4], 6, (1, 3)),
        ([-1, 0], -1, (1, 2)),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, (4, 5)),
    ],
)
def test_examples(nums, target, expected):
    assert two_sum_sorted(nums, target) == expected

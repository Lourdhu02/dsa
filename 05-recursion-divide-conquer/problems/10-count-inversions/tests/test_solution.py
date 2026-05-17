import pytest

from solution import count_inversions


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 5, 2, 4, 6], 3),
        ([5, 4, 3, 2, 1], 10),
        ([1, 2, 3], 0),
        ([], 0),
        ([2, 4, 1, 3, 5], 3),
    ],
)
def test_examples(nums, expected):
    assert count_inversions(nums) == expected

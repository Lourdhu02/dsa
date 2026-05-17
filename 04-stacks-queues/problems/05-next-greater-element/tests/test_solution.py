import pytest

from solution import next_greater


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 1, 2, 4, 3], [4, 2, 4, -1, -1]),
        ([1, 2, 3, 4], [2, 3, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),
        ([], []),
        ([5], [-1]),
    ],
)
def test_examples(nums, expected):
    assert next_greater(nums) == expected

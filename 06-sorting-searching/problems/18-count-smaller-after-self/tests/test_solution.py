import pytest
from solution import count_smaller


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([-1], [0]),
        ([-1, -1], [0, 0]),
        ([2, 0, 1], [2, 0, 0]),
    ],
)
def test_examples(nums, expected):
    assert count_smaller(nums) == expected

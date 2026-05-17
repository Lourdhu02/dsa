import pytest

from solution import product_except_self


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([5, 6], [6, 5]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ],
)
def test_examples(nums, expected):
    assert product_except_self(nums) == expected

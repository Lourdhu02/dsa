import pytest
from solution import count_range_sum


@pytest.mark.parametrize(
    "nums, lo, up, expected",
    [([-2, 5, -1], -2, 2, 3), ([0], 0, 0, 1), ([1, 2, 3], 3, 5, 4)],
)
def test_examples(nums, lo, up, expected):
    assert count_range_sum(nums, lo, up) == expected

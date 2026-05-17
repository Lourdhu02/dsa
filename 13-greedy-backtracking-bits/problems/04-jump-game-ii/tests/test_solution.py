import pytest
from solution import jump


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, 1, 1, 4], 2), ([2, 3, 0, 1, 4], 2), ([0], 0), ([1, 2], 1)],
)
def test_examples(nums, expected):
    assert jump(nums) == expected

import pytest
from solution import max_product


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, -2, 4], 6), ([-2, 0, -1], 0), ([-2, 3, -4], 24), ([0, 2], 2)],
)
def test_examples(nums, expected):
    assert max_product(nums) == expected

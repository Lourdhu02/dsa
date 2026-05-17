import pytest
from solution import find_maximum_xor


@pytest.mark.parametrize(
    "nums, expected",
    [([3, 10, 5, 25, 2, 8], 28), ([0], 0), ([1, 2], 3), ([8, 10, 2], 10)],
)
def test_examples(nums, expected):
    assert find_maximum_xor(nums) == expected

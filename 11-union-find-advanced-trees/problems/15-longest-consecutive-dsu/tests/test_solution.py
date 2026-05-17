import pytest
from solution import longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [([100, 4, 200, 1, 3, 2], 4), ([], 0), ([1, 2, 0, 1], 3)],
)
def test_examples(nums, expected):
    assert longest_consecutive(nums) == expected

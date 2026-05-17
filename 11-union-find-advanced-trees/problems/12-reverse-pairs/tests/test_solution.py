import pytest
from solution import reverse_pairs


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 3, 2, 3, 1], 2), ([2, 4, 3, 5, 1], 3), ([], 0), ([5], 0)],
)
def test_examples(nums, expected):
    assert reverse_pairs(nums) == expected

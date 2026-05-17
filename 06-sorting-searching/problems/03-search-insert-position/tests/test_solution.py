import pytest
from solution import search_insert


@pytest.mark.parametrize(
    "nums, target, expected",
    [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4), ([], 5, 0)],
)
def test_examples(nums, target, expected):
    assert search_insert(nums, target) == expected

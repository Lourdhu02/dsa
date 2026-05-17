import pytest
from solution import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12], 2, -1), ([], 1, -1), ([1], 1, 0)],
)
def test_examples(nums, target, expected):
    assert search(nums, target) == expected

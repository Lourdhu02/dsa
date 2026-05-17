import pytest

from solution import contains_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([], False), ([1], False), ([1, 1], True)],
)
def test_examples(nums, expected):
    assert contains_duplicate(nums) == expected

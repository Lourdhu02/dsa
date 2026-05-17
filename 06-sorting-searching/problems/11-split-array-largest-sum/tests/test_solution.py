import pytest
from solution import split_array


@pytest.mark.parametrize(
    "nums, k, expected",
    [([7, 2, 5, 10, 8], 2, 18), ([1, 2, 3, 4, 5], 2, 9), ([1, 4, 4], 3, 4)],
)
def test_examples(nums, k, expected):
    assert split_array(nums, k) == expected

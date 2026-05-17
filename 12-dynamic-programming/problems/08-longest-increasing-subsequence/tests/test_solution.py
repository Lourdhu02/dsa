import pytest
from solution import length_of_lis


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([], 0),
    ],
)
def test_examples(nums, expected):
    assert length_of_lis(nums) == expected

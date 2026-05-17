import pytest

from solution import min_subarray_len


@pytest.mark.parametrize(
    "target, nums, expected",
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
        (100, [100], 1),
    ],
)
def test_examples(target, nums, expected):
    assert min_subarray_len(target, nums) == expected

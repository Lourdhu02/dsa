import pytest

from solution import rotate


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1], 5, [1]),
        ([], 3, []),
        ([1, 2], 4, [1, 2]),
    ],
)
def test_examples(nums, k, expected):
    rotate(nums, k)
    assert nums == expected

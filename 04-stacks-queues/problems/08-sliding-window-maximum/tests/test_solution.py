import pytest

from solution import max_sliding_window


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
    ],
)
def test_examples(nums, k, expected):
    assert max_sliding_window(nums, k) == expected

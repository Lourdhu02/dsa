import pytest

from solution import max_sum_k


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([5, 5, 5, 5], 2, 10),
        ([7], 1, 7),
        ([1, 2, 3, 4, 5], 5, 15),
        ([-1, -2, -3, -4], 2, -3),
    ],
)
def test_examples(nums, k, expected):
    assert max_sum_k(nums, k) == expected


def test_invalid_k_raises():
    with pytest.raises(ValueError):
        max_sum_k([1, 2, 3], 0)
    with pytest.raises(ValueError):
        max_sum_k([1, 2, 3], 4)

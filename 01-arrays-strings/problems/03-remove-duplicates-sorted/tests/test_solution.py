import pytest

from solution import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected_k, expected_prefix",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([7], 1, [7]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ],
)
def test_remove_duplicates(nums, expected_k, expected_prefix):
    k = remove_duplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_prefix

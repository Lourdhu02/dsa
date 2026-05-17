import pytest
from solution import top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected",
    [([1, 1, 1, 2, 2, 3], 2, {1, 2}), ([1], 1, {1}), ([4, 4, 5, 6, 6], 2, {4, 6})],
)
def test_examples(nums, k, expected):
    assert set(top_k_frequent(nums, k)) == expected

import pytest

from solution import top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected_set",
    [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 5, 5, 6], 2, {4, 5}),
    ],
)
def test_examples(nums, k, expected_set):
    assert set(top_k_frequent(nums, k)) == expected_set

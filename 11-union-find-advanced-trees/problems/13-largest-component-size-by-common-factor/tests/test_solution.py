import pytest
from solution import largest_component_size


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([4, 6, 15, 35], 4),
        ([20, 50, 9, 63], 2),
        ([2, 3, 6, 7, 4, 12, 21, 39], 8),
    ],
)
def test_examples(nums, expected):
    assert largest_component_size(nums) == expected

import pytest
from solution import single_number


@pytest.mark.parametrize("nums, expected", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([7], 7)])
def test_examples(nums, expected):
    assert single_number(nums) == expected

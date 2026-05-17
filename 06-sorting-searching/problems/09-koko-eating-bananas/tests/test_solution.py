import pytest
from solution import min_eating_speed


@pytest.mark.parametrize(
    "piles, h, expected",
    [([3, 6, 7, 11], 8, 4), ([30, 11, 23, 4, 20], 5, 30), ([1], 1, 1)],
)
def test_examples(piles, h, expected):
    assert min_eating_speed(piles, h) == expected

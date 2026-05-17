import pytest
from solution import furthest_building


@pytest.mark.parametrize(
    "heights, bricks, ladders, expected",
    [([4, 2, 7, 6, 9, 14, 12], 5, 1, 4), ([14, 3, 19, 3], 17, 0, 3)],
)
def test_examples(heights, bricks, ladders, expected):
    assert furthest_building(heights, bricks, ladders) == expected

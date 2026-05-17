import pytest
from solution import swim_in_water


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 2], [1, 3]], 3),
        ([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16),
    ],
)
def test_examples(grid, expected):
    assert swim_in_water(grid) == expected

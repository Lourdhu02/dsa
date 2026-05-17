import pytest
from solution import shortest_path


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ],
)
def test_examples(grid, expected):
    assert shortest_path(grid) == expected

import pytest
from solution import unique_paths_with_obstacles


@pytest.mark.parametrize(
    "grid, expected",
    [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2), ([[0, 1], [0, 0]], 1), ([[1]], 0)],
)
def test_examples(grid, expected):
    assert unique_paths_with_obstacles(grid) == expected

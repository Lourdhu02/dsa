import pytest
from solution import min_cost_connect


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
        ([[0, 0]], 0),
    ],
)
def test_examples(points, expected):
    assert min_cost_connect(points) == expected

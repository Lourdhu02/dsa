import pytest
from solution import mst_cost


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 10]], 6),
        (3, [[0, 1, 5]], -1),
    ],
)
def test_examples(n, edges, expected):
    assert mst_cost(n, edges) == expected

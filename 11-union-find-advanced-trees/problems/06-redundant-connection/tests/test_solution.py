import pytest
from solution import find_redundant_connection


@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ],
)
def test_examples(edges, expected):
    assert find_redundant_connection(edges) == expected

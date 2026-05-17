import pytest
from solution import is_bipartite


@pytest.mark.parametrize(
    "graph, expected",
    [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
        ([], True),
    ],
)
def test_examples(graph, expected):
    assert is_bipartite(graph) is expected

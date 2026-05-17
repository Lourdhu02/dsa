import pytest
from solution import valid_tree


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
        (1, [], True),
    ],
)
def test_examples(n, edges, expected):
    assert valid_tree(n, edges) is expected

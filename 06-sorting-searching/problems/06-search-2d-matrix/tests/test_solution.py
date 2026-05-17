import pytest
from solution import search_matrix


M = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        (M, 3, True),
        (M, 13, False),
        ([], 1, False),
        ([[1]], 1, True),
    ],
)
def test_examples(matrix, target, expected):
    assert search_matrix(matrix, target) is expected

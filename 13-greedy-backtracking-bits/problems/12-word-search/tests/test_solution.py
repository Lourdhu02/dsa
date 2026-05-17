import pytest
from solution import exist


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]


@pytest.mark.parametrize(
    "word, expected",
    [("ABCCED", True), ("SEE", True), ("ABCB", False)],
)
def test_examples(word, expected):
    assert exist([row[:] for row in board], word) is expected

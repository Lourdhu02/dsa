import pytest
from solution import can_finish


@pytest.mark.parametrize(
    "n, prereqs, expected",
    [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False), (4, [[1, 0], [2, 1], [3, 2]], True)],
)
def test_examples(n, prereqs, expected):
    assert can_finish(n, prereqs) is expected

import pytest
from solution import merge


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([], []),
        ([[1, 4], [0, 4]], [[0, 4]]),
    ],
)
def test_examples(intervals, expected):
    assert merge(intervals) == expected

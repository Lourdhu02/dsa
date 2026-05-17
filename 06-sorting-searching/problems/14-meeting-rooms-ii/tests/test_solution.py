import pytest
from solution import min_meeting_rooms


@pytest.mark.parametrize(
    "intervals, expected",
    [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1), ([], 0), ([[1, 5]], 1)],
)
def test_examples(intervals, expected):
    assert min_meeting_rooms(intervals) == expected

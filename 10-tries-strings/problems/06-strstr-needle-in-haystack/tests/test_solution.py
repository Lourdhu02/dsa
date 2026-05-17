import pytest
from solution import str_str


@pytest.mark.parametrize(
    "h, n, expected",
    [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1), ("abc", "", 0), ("a", "a", 0)],
)
def test_examples(h, n, expected):
    assert str_str(h, n) == expected

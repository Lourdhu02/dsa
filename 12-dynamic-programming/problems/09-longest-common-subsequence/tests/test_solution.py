import pytest
from solution import lcs


@pytest.mark.parametrize(
    "s, t, expected",
    [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0), ("", "abc", 0)],
)
def test_examples(s, t, expected):
    assert lcs(s, t) == expected

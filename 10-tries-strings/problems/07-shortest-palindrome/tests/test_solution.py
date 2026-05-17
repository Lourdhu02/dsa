import pytest
from solution import shortest_palindrome


@pytest.mark.parametrize(
    "s, expected", [("aacecaaa", "aaacecaaa"), ("abcd", "dcbabcd"), ("", ""), ("a", "a")]
)
def test_examples(s, expected):
    assert shortest_palindrome(s) == expected

import pytest
from solution import repeated_substring_pattern


@pytest.mark.parametrize(
    "s, expected",
    [("abab", True), ("aba", False), ("abcabcabcabc", True), ("", False), ("a", False)],
)
def test_examples(s, expected):
    assert repeated_substring_pattern(s) is expected

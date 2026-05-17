import pytest

from solution import is_anagram


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "ab", False),
        ("aabb", "abab", True),
    ],
)
def test_examples(s, t, expected):
    assert is_anagram(s, t) == expected

import pytest

from solution import word_pattern


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog dog dog dog", True),
        ("abba", "dog dog dog dog", False),
        ("aaa", "dog cat dog", False),
    ],
)
def test_examples(pattern, s, expected):
    assert word_pattern(pattern, s) == expected

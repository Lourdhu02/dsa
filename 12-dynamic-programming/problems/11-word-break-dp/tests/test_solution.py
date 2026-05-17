import pytest
from solution import word_break


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_examples(s, words, expected):
    assert word_break(s, words) is expected

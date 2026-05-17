import pytest

from solution import longest_palindrome


@pytest.mark.parametrize(
    "s, valid_answers",
    [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),
        ("racecar", {"racecar"}),
        ("", {""}),
    ],
)
def test_examples(s, valid_answers):
    assert longest_palindrome(s) in valid_answers

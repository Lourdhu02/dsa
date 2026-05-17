import pytest

from solution import decode_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc", "abc"),
        ("10[a]", "aaaaaaaaaa"),
    ],
)
def test_examples(s, expected):
    assert decode_string(s) == expected

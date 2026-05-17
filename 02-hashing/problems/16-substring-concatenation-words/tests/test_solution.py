import pytest

from solution import find_substring


def _norm(xs):
    return sorted(xs)


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ],
)
def test_examples(s, words, expected):
    assert _norm(find_substring(s, words)) == _norm(expected)

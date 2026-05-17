import pytest

from solution import reverse_string


@pytest.mark.parametrize(
    "given, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["a"], ["a"]),
        ([], []),
        (["a", "b"], ["b", "a"]),
        (list("abcdef"), list("fedcba")),
    ],
)
def test_reverse_string(given, expected):
    reverse_string(given)
    assert given == expected


def test_returns_none():
    s = ["a", "b", "c"]
    assert reverse_string(s) is None

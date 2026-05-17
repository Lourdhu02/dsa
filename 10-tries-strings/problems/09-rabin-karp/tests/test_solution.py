import pytest
from solution import rabin_karp


@pytest.mark.parametrize(
    "text, pat, expected",
    [
        ("abracadabra", "abra", [0, 7]),
        ("aaaa", "aa", [0, 1, 2]),
        ("abc", "d", []),
        ("abc", "", [0, 1, 2, 3]),
    ],
)
def test_examples(text, pat, expected):
    assert rabin_karp(text, pat) == expected

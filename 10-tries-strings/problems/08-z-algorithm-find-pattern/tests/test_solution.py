import pytest
from solution import z_find


@pytest.mark.parametrize(
    "text, pat, expected",
    [
        ("aaaaa", "aa", [0, 1, 2, 3]),
        ("abracadabra", "abra", [0, 7]),
        ("abc", "d", []),
    ],
)
def test_examples(text, pat, expected):
    assert z_find(text, pat) == expected

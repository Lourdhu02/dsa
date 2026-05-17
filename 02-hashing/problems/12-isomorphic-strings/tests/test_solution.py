import pytest

from solution import is_isomorphic


@pytest.mark.parametrize(
    "s, t, expected",
    [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True), ("ab", "aa", False), ("", "", True)],
)
def test_examples(s, t, expected):
    assert is_isomorphic(s, t) == expected

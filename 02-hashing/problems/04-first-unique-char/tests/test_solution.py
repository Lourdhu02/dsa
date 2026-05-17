import pytest

from solution import first_uniq_char


@pytest.mark.parametrize(
    "s, expected",
    [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1), ("z", 0), ("", -1)],
)
def test_examples(s, expected):
    assert first_uniq_char(s) == expected

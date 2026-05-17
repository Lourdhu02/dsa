import pytest

from solution import group_anagrams


def _norm(groups):
    return sorted(tuple(sorted(g)) for g in groups)


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_examples(strs, expected):
    assert _norm(group_anagrams(strs)) == _norm(expected)

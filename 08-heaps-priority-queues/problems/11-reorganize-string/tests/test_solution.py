from solution import reorganize_string


def _valid(s, t):
    if not t:
        return False
    from collections import Counter
    if Counter(s) != Counter(t):
        return False
    return all(t[i] != t[i + 1] for i in range(len(t) - 1))


def test_possible():
    s = "aab"
    out = reorganize_string(s)
    assert _valid(s, out)


def test_impossible():
    assert reorganize_string("aaab") == ""

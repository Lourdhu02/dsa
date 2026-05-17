from solution import palindrome_pairs


def _norm(pairs):
    return sorted(tuple(p) for p in pairs)


def test_basic():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    assert _norm(palindrome_pairs(words)) == _norm([[0, 1], [1, 0], [3, 2], [2, 4]])


def test_with_empty():
    words = ["a", ""]
    assert _norm(palindrome_pairs(words)) == _norm([[0, 1], [1, 0]])

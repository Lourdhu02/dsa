from solutions.kmp import build_failure, kmp_find_all
from solutions.trie import Trie


def test_trie_basic():
    t = Trie()
    t.insert("apple")
    t.insert("app")
    assert t.contains("apple")
    assert t.contains("app")
    assert not t.contains("ap")
    assert t.startswith("ap")
    assert not t.startswith("ban")


def test_failure_table():
    assert build_failure("abacab") == [0, 0, 1, 0, 1, 2]
    assert build_failure("aaaaa") == [0, 1, 2, 3, 4]


def test_kmp_find_all():
    assert kmp_find_all("abxabcabcaby", "abcaby") == [6]
    assert kmp_find_all("aaaaa", "aa") == [0, 1, 2, 3]
    assert kmp_find_all("abc", "") == [0, 1, 2, 3]
    assert kmp_find_all("", "abc") == []

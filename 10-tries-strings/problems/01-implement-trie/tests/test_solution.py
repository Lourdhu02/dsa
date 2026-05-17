from solution import Trie


def test_basic_flow():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startswith("app") is True
    t.insert("app")
    assert t.search("app") is True

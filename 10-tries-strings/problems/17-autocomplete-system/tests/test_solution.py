from solution import AutocompleteSystem


def test_basic_sequence():
    ac = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    assert ac.input("i") == ["i love you", "island", "i love leetcode"]
    assert ac.input(" ") == ["i love you", "i love leetcode"]
    assert ac.input("a") == []
    assert ac.input("#") == []

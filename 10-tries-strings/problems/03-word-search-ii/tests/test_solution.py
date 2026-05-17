from solution import find_words


def test_basic():
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(find_words([row[:] for row in board], words)) == sorted(["oath", "eat"])


def test_empty_board():
    assert find_words([], ["a"]) == []

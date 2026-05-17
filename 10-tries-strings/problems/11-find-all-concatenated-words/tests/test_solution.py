from solution import find_all_concatenated_words


def test_basic():
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    assert sorted(find_all_concatenated_words(words)) == sorted(["catsdogcats", "dogcatsdog", "ratcatdogcat"])


def test_no_concat():
    assert find_all_concatenated_words(["a", "b", "c"]) == []

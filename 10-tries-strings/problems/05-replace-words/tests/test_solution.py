from solution import replace_words


def test_basic():
    assert replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"


def test_no_change():
    assert replace_words(["abc"], "hello world") == "hello world"

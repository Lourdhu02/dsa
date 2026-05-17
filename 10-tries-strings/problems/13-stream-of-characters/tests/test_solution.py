from solution import StreamChecker


def test_basic_sequence():
    sc = StreamChecker(["cd", "f", "kl"])
    assert sc.query("a") is False
    assert sc.query("b") is False
    assert sc.query("c") is False
    assert sc.query("d") is True
    assert sc.query("e") is False
    assert sc.query("f") is True

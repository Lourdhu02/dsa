from solution import greet


def test_greet_returns_expected_string():
    assert greet() == "hello, pytest"

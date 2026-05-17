import pytest

from solution import is_palindrome_number


@pytest.mark.parametrize(
    "n, expected",
    [(121, True), (-121, False), (10, False), (0, True), (1234321, True), (123, False), (11, True)],
)
def test_examples(n, expected):
    assert is_palindrome_number(n) == expected


def test_agrees_with_string_check():
    for n in range(0, 10_000):
        assert is_palindrome_number(n) == (str(n) == str(n)[::-1])

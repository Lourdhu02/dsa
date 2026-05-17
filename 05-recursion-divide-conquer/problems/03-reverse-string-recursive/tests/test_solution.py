import pytest

from solution import reverse_string


@pytest.mark.parametrize(
    "given, expected",
    [(list("hello"), list("olleh")), ([], []), (["a"], ["a"]), (list("abc"), list("cba"))],
)
def test_examples(given, expected):
    reverse_string(given)
    assert given == expected

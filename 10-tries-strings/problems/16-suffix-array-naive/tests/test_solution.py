import pytest
from solution import suffix_array


@pytest.mark.parametrize(
    "s, expected",
    [("banana", [5, 3, 1, 0, 4, 2]), ("abc", [0, 1, 2]), ("", [])],
)
def test_examples(s, expected):
    assert suffix_array(s) == expected

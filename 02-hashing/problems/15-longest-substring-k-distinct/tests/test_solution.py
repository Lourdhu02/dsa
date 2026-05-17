import pytest

from solution import longest_at_most_k


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("eceba", 2, 3),
        ("aa", 1, 2),
        ("abcadcacacaca", 3, 11),
        ("", 2, 0),
        ("abc", 0, 0),
    ],
)
def test_examples(s, k, expected):
    assert longest_at_most_k(s, k) == expected

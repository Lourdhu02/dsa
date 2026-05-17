import pytest

from solution import calculate


@pytest.mark.parametrize(
    "s, expected",
    [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("0", 0),
        ("-(1+2)", -3),
    ],
)
def test_examples(s, expected):
    assert calculate(s) == expected

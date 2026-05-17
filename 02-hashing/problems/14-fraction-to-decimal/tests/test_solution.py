import pytest

from solution import fraction_to_decimal


@pytest.mark.parametrize(
    "n, d, expected",
    [
        (1, 2, "0.5"),
        (2, 1, "2"),
        (4, 333, "0.(012)"),
        (1, 3, "0.(3)"),
        (0, 5, "0"),
        (-1, 2, "-0.5"),
    ],
)
def test_examples(n, d, expected):
    assert fraction_to_decimal(n, d) == expected

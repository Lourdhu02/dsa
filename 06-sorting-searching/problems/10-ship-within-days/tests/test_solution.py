import pytest
from solution import ship_within_days


@pytest.mark.parametrize(
    "weights, days, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
    ],
)
def test_examples(weights, days, expected):
    assert ship_within_days(weights, days) == expected

import pytest

from solution import daily_temperatures


@pytest.mark.parametrize(
    "temps, expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80], [0, 0]),
    ],
)
def test_examples(temps, expected):
    assert daily_temperatures(temps) == expected

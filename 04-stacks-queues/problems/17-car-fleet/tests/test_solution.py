import pytest

from solution import car_fleet


@pytest.mark.parametrize(
    "target, pos, speed, expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
    ],
)
def test_examples(target, pos, speed, expected):
    assert car_fleet(target, pos, speed) == expected

import pytest

from solution import asteroid_collision


@pytest.mark.parametrize(
    "a, expected",
    [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([], []),
    ],
)
def test_examples(a, expected):
    assert asteroid_collision(a) == expected

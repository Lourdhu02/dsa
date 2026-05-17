import pytest

from solution import move_zeros


@pytest.mark.parametrize(
    "given, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
    ],
)
def test_examples(given, expected):
    move_zeros(given)
    assert given == expected

import pytest
from solution import find_circle_num


@pytest.mark.parametrize(
    "m, expected",
    [([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2), ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)],
)
def test_examples(m, expected):
    assert find_circle_num(m) == expected

import pytest

from solution import largest_rectangle


@pytest.mark.parametrize(
    "h, expected",
    [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([], 0),
        ([1, 1, 1, 1], 4),
        ([6, 7, 5, 2, 4, 5, 9, 3], 16),
    ],
)
def test_examples(h, expected):
    assert largest_rectangle(h) == expected

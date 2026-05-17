import pytest
from solution import sort_colors


@pytest.mark.parametrize(
    "given, expected",
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([], []),
    ],
)
def test_examples(given, expected):
    sort_colors(given)
    assert given == expected

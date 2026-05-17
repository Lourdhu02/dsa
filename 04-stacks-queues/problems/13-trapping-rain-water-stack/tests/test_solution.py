import pytest

from solution import trap


@pytest.mark.parametrize(
    "h, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([3], 0),
    ],
)
def test_examples(h, expected):
    assert trap(h) == expected

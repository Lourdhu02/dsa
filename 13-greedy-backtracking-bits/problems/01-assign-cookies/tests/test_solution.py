import pytest
from solution import find_content_children


@pytest.mark.parametrize(
    "g, s, expected",
    [([1, 2, 3], [1, 1], 1), ([1, 2], [1, 2, 3], 2), ([10], [1, 1, 1], 0)],
)
def test_examples(g, s, expected):
    assert find_content_children(g, s) == expected

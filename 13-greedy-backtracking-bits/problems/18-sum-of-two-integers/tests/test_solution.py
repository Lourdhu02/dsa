import pytest
from solution import get_sum


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (-1, 1, 0), (-2, 3, 1), (0, 0, 0), (5, 5, 10)])
def test_examples(a, b, expected):
    assert get_sum(a, b) == expected

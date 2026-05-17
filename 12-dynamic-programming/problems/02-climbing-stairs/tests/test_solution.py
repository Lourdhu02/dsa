import pytest
from solution import climb_stairs


@pytest.mark.parametrize("n, expected", [(1, 1), (2, 2), (3, 3), (5, 8), (10, 89)])
def test_examples(n, expected):
    assert climb_stairs(n) == expected

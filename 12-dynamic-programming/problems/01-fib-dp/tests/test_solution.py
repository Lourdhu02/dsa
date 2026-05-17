import pytest
from solution import fib


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (10, 55), (30, 832040)])
def test_examples(n, expected):
    assert fib(n) == expected

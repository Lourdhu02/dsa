import pytest
from solution import count_bits


@pytest.mark.parametrize("n, expected", [(5, [0, 1, 1, 2, 1, 2]), (2, [0, 1, 1]), (0, [0])])
def test_examples(n, expected):
    assert count_bits(n) == expected

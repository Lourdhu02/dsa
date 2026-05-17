import pytest
from solution import is_perfect_square


@pytest.mark.parametrize(
    "n, expected", [(16, True), (14, False), (1, True), (0, True), (2147395600, True)]
)
def test_examples(n, expected):
    assert is_perfect_square(n) is expected

import pytest

from solution import is_happy


@pytest.mark.parametrize("n, expected", [(19, True), (2, False), (1, True), (7, True), (4, False)])
def test_examples(n, expected):
    assert is_happy(n) == expected

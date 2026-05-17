import math
import pytest

from solution import factorial


@pytest.mark.parametrize("n", [0, 1, 2, 5, 10, 20])
def test_matches_stdlib(n):
    assert factorial(n) == math.factorial(n)


def test_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)

import pytest
from solution import find_maximized_capital


@pytest.mark.parametrize(
    "k, w, profits, capital, expected",
    [(2, 0, [1, 2, 3], [0, 1, 1], 4), (3, 0, [1, 2, 3], [0, 1, 2], 6)],
)
def test_examples(k, w, profits, capital, expected):
    assert find_maximized_capital(k, w, profits, capital) == expected

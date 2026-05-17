import pytest

from solution import hanoi


@pytest.mark.parametrize("n", [0, 1, 2, 3, 5, 10])
def test_move_count_is_2n_minus_1(n):
    assert len(hanoi(n)) == (2**n - 1)


def test_n_equals_2():
    assert hanoi(2) == [("A", "B"), ("A", "C"), ("B", "C")]

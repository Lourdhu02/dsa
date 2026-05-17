import pytest
from solution import solve_n_queens


def test_n4():
    res = solve_n_queens(4)
    assert len(res) == 2
    assert all(len(b) == 4 and all(len(r) == 4 for r in b) for b in res)


def test_n1():
    assert solve_n_queens(1) == [["Q"]]

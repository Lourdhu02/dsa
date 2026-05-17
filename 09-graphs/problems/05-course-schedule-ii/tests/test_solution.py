import pytest
from solution import find_order


def _validate(n, prereqs, order):
    if not order:
        return False
    pos = {c: i for i, c in enumerate(order)}
    if len(pos) != n:
        return False
    return all(pos[b] < pos[a] for a, b in prereqs)


def test_basic():
    order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert _validate(4, [[1, 0], [2, 0], [3, 1], [3, 2]], order)


def test_cycle():
    assert find_order(2, [[0, 1], [1, 0]]) == []

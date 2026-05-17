import pytest
from solution import critical_connections


def _norm(es):
    return sorted(tuple(sorted(e)) for e in es)


def test_basic():
    assert _norm(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])) == [(1, 3)]


def test_no_bridges():
    assert critical_connections(3, [[0, 1], [1, 2], [2, 0]]) == []

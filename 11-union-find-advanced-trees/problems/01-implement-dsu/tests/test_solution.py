from solution import DSU


def test_basic():
    d = DSU(5)
    assert d.count == 5
    assert d.union(0, 1)
    assert not d.union(0, 1)
    assert d.connected(0, 1)
    assert not d.connected(0, 2)
    assert d.count == 4

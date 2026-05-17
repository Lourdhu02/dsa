from solution import NumArrayMin


def test_basic():
    nm = NumArrayMin([5, 2, 6, 1, 4])
    assert nm.range_min(0, 4) == 1
    nm.update(3, 100)
    assert nm.range_min(0, 4) == 2
    assert nm.range_min(0, 0) == 5

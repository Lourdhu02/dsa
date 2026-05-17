from solution import NumArray


def test_basic():
    na = NumArray([1, 3, 5])
    assert na.sum_range(0, 2) == 9
    na.update(1, 2)
    assert na.sum_range(0, 2) == 8

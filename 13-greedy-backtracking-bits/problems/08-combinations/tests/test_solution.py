from solution import combine


def test_basic():
    assert sorted(map(tuple, combine(4, 2))) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_n_eq_k():
    assert combine(3, 3) == [[1, 2, 3]]

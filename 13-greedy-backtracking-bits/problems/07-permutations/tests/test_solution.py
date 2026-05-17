from solution import permute


def test_three():
    res = permute([1, 2, 3])
    assert sorted(map(tuple, res)) == sorted([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])


def test_empty():
    assert permute([]) == [[]]

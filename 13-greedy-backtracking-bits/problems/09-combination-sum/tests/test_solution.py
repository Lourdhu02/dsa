from solution import combination_sum


def test_basic():
    res = combination_sum([2, 3, 6, 7], 7)
    assert sorted(map(tuple, res)) == sorted([(2, 2, 3), (7,)])


def test_no_solution():
    assert combination_sum([2, 4], 7) == []

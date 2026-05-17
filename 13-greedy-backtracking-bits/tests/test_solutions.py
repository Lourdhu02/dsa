from solutions.backtrack import combinations, permutations
from solutions.bits import clear_lowest_set_bit, iter_submasks, lowest_set_bit
from solutions.greedy import activity_selection


def test_activity_selection():
    assert activity_selection([(1, 3), (2, 4), (3, 5), (5, 7)]) == 3


def test_permutations_count():
    perms = permutations([1, 2, 3])
    assert len(perms) == 6
    assert all(sorted(p) == [1, 2, 3] for p in perms)


def test_combinations():
    cs = combinations(4, 2)
    assert sorted(map(tuple, cs)) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_lowest_set_bit():
    assert lowest_set_bit(12) == 4
    assert lowest_set_bit(1) == 1
    assert lowest_set_bit(0) == 0


def test_clear_lowest_set_bit():
    assert clear_lowest_set_bit(0b1010) == 0b1000


def test_iter_submasks():
    submasks = list(iter_submasks(0b101))
    assert submasks == [0b101, 0b100, 0b001]

from solutions.kadane import kadane
from solutions.prefix_sum import PrefixSum
from solutions.sliding_window import fixed_window_max_sum
from solutions.two_pointer import converging, same_direction_compact


def test_two_pointer_converging():
    assert converging([1, 2, 4, 7, 11, 15], 9) == (1, 3)
    assert converging([1, 2, 3], 10) is None


def test_same_direction_compact_removes_zeros():
    xs = [1, 0, 2, 0, 3, 0, 4]
    n = same_direction_compact(xs, lambda v: v != 0)
    assert xs[:n] == [1, 2, 3, 4]


def test_fixed_window_max_sum():
    assert fixed_window_max_sum([2, 1, 5, 1, 3, 2], 3) == 9
    assert fixed_window_max_sum([5], 1) == 5


def test_prefix_sum_range_query():
    p = PrefixSum([3, 1, 4, 1, 5, 9, 2, 6])
    assert p.range_sum(0, 4) == 9
    assert p.range_sum(2, 6) == 19
    assert p.range_sum(0, 0) == 0


def test_kadane_classic_case():
    # The canonical example from Programming Pearls (1986), Ch.8.
    assert kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert kadane([-1, -2, -3]) == -1
    assert kadane([5]) == 5

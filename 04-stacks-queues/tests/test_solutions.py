from solutions.monotonic import next_greater_right, sliding_window_max


def test_next_greater_basic():
    assert next_greater_right([2, 1, 2, 4, 3, 1]) == [4, 2, 4, -1, -1, -1]
    assert next_greater_right([]) == []
    assert next_greater_right([5]) == [-1]


def test_sliding_window_max_basic():
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max([1], 1) == [1]
    assert sliding_window_max([9, 11], 2) == [11]

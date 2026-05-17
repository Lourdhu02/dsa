from solutions.dp import edit_distance, knapsack_01, knapsack_unbounded, lis_length


def test_knapsack_01():
    assert knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
    assert knapsack_01([], [], 10) == 0


def test_knapsack_unbounded():
    assert knapsack_unbounded([1, 3, 4], [10, 40, 50], 8) == 110


def test_lis_length():
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([0, 1, 0, 3, 2, 3]) == 4
    assert lis_length([7, 7, 7, 7]) == 1
    assert lis_length([]) == 0


def test_edit_distance():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "") == 3
    assert edit_distance("same", "same") == 0

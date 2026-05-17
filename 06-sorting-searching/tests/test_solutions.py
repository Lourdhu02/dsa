import random

from solutions.binary_search import first_true, lower_bound, search_exact, upper_bound
from solutions.sorts import counting_sort, insertion_sort, selection_sort


def test_search_exact():
    a = [1, 3, 5, 7, 9, 11]
    assert search_exact(a, 7) == 3
    assert search_exact(a, 4) == -1
    assert search_exact([], 1) == -1


def test_lower_upper_match_bisect():
    from bisect import bisect_left, bisect_right

    a = [1, 2, 2, 2, 5, 5, 9]
    for t in (-1, 0, 1, 2, 5, 6, 9, 10):
        assert lower_bound(a, t) == bisect_left(a, t)
        assert upper_bound(a, t) == bisect_right(a, t)


def test_first_true_on_simple_predicate():
    # smallest x in [0, 100] with x * x >= 50
    assert first_true(0, 100, lambda x: x * x >= 50) == 8


def test_insertion_sort_matches_sorted():
    rng = random.Random(2)
    for _ in range(10):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 60))]
        assert insertion_sort(xs) == sorted(xs)


def test_selection_sort_matches_sorted():
    rng = random.Random(3)
    for _ in range(10):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 60))]
        assert selection_sort(xs) == sorted(xs)


def test_counting_sort_matches_sorted():
    rng = random.Random(4)
    for _ in range(10):
        xs = [rng.randint(0, 30) for _ in range(rng.randint(0, 200))]
        assert counting_sort(xs) == sorted(xs)

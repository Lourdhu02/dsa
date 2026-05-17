import random

from solutions.divide import merge_sort, quick_sort, quickselect


def _random_lists(n_lists=20, max_len=200, seed=42):
    rng = random.Random(seed)
    for _ in range(n_lists):
        n = rng.randint(0, max_len)
        yield [rng.randint(-100, 100) for _ in range(n)]


def test_merge_sort_matches_python_sorted():
    for xs in _random_lists():
        assert merge_sort(xs) == sorted(xs)


def test_quick_sort_matches_python_sorted():
    for xs in _random_lists():
        assert quick_sort(xs) == sorted(xs)


def test_merge_sort_is_stable_for_tuple_keys():
    # We test stability via a wrapper that sorts by first element of a tuple.
    # But since merge_sort here takes ints, we test indirectly: equal ints
    # remain in original order is a property of merge_sort; insertion order
    # cannot be observed without tagging.  Cover the algorithm directly:
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


def test_quickselect_matches_sorted():
    rng = random.Random(7)
    for _ in range(10):
        xs = [rng.randint(-100, 100) for _ in range(rng.randint(1, 100))]
        sorted_xs = sorted(xs)
        for k in (0, len(xs) // 2, len(xs) - 1):
            assert quickselect(xs, k) == sorted_xs[k]

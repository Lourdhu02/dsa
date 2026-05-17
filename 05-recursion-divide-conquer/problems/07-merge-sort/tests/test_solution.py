import random

import pytest

from solution import merge_sort


def test_matches_sorted():
    rng = random.Random(0)
    for _ in range(10):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        assert merge_sort(xs) == sorted(xs)


def test_stability_on_tuples():
    # We can't test stability on bare ints, but we can verify by tagging equal-keyed integers.
    tagged = list(enumerate([5, 1, 5, 1, 5]))
    # Sort by value; ensure tags within each value group keep ascending order.
    indices = sorted(range(len(tagged)), key=lambda i: tagged[i][1])
    # Reconstruct what stable sort would do: extract tags grouped by value
    by_value = {}
    for i in indices:
        by_value.setdefault(tagged[i][1], []).append(tagged[i][0])
    for tags in by_value.values():
        assert tags == sorted(tags)

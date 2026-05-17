import pytest
from solution import k_closest


def _sq_dists(points):
    return sorted(p[0] ** 2 + p[1] ** 2 for p in points)


@pytest.mark.parametrize(
    "points, k",
    [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
    ],
)
def test_distance_sets_match(points, k):
    result = k_closest(points, k)
    assert len(result) == k
    # Closest k distances should match
    all_dists = sorted(p[0] ** 2 + p[1] ** 2 for p in points)[:k]
    assert _sq_dists(result) == all_dists

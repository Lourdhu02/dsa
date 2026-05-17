import pytest

from solution import three_sum


def _norm(triplets):
    return sorted(tuple(sorted(t)) for t in triplets)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ],
)
def test_examples(nums, expected):
    assert _norm(three_sum(nums)) == _norm(expected)

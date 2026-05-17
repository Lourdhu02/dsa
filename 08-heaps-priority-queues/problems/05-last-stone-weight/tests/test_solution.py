import pytest
from solution import last_stone_weight


@pytest.mark.parametrize(
    "stones, expected",
    [([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([3, 3], 0), ([2, 2, 1], 1)],
)
def test_examples(stones, expected):
    assert last_stone_weight(stones) == expected

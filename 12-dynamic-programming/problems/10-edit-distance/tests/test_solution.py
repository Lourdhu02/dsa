import pytest
from solution import min_distance


@pytest.mark.parametrize(
    "s, t, expected",
    [("horse", "ros", 3), ("intention", "execution", 5), ("", "abc", 3), ("same", "same", 0)],
)
def test_examples(s, t, expected):
    assert min_distance(s, t) == expected

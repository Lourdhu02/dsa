import pytest
from solution import num_distinct


@pytest.mark.parametrize(
    "s, t, expected",
    [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5), ("a", "", 1), ("", "a", 0)],
)
def test_examples(s, t, expected):
    assert num_distinct(s, t) == expected

import pytest
from solution import partition_labels


@pytest.mark.parametrize(
    "s, expected",
    [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10]), ("a", [1])],
)
def test_examples(s, expected):
    assert partition_labels(s) == expected

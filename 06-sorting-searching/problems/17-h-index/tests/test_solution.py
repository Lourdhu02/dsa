import pytest
from solution import h_index


@pytest.mark.parametrize(
    "citations, expected",
    [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1), ([], 0), ([100], 1), ([0, 0, 0], 0)],
)
def test_examples(citations, expected):
    assert h_index(citations) == expected

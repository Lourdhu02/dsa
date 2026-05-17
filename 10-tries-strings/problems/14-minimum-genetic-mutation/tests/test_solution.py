import pytest
from solution import min_mutation


@pytest.mark.parametrize(
    "s, e, bank, expected",
    [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
        ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3),
    ],
)
def test_examples(s, e, bank, expected):
    assert min_mutation(s, e, bank) == expected

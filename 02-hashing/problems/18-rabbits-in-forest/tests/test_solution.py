import pytest

from solution import num_rabbits


@pytest.mark.parametrize(
    "answers, expected",
    [([1, 1, 2], 5), ([10, 10, 10], 11), ([], 0), ([0, 0, 1, 1, 1], 6)],
)
def test_examples(answers, expected):
    assert num_rabbits(answers) == expected

import pytest
from solution import least_interval


@pytest.mark.parametrize(
    "tasks, n, expected",
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "D", "B"], 1, 6),
        (["A"], 0, 1),
    ],
)
def test_examples(tasks, n, expected):
    assert least_interval(tasks, n) == expected

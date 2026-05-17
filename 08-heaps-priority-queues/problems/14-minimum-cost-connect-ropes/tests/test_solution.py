import pytest
from solution import connect_ropes


@pytest.mark.parametrize(
    "ropes, expected",
    [([1, 2, 3, 4, 5], 33), ([4, 3, 2, 6], 29), ([1], 0), ([], 0)],
)
def test_examples(ropes, expected):
    assert connect_ropes(ropes) == expected

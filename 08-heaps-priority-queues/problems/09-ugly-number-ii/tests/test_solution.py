import pytest
from solution import nth_ugly


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (10, 12), (11, 15), (1690, 2123366400)]
)
def test_examples(n, expected):
    assert nth_ugly(n) == expected

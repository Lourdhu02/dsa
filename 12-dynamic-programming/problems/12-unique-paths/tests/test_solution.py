import pytest
from solution import unique_paths


@pytest.mark.parametrize("m, n, expected", [(3, 7, 28), (3, 2, 3), (1, 1, 1)])
def test_examples(m, n, expected):
    assert unique_paths(m, n) == expected

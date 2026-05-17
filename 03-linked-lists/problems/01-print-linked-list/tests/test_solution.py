import pytest

from solution import build, to_list


@pytest.mark.parametrize("xs", [[], [1], [1, 2, 3], list(range(50))])
def test_roundtrip(xs):
    assert to_list(build(xs)) == xs

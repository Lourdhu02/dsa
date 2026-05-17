import pytest

from solution import first_bad_version


@pytest.mark.parametrize(
    "n, first_bad",
    [(5, 4), (1, 1), (10, 7), (100, 50)],
)
def test_finds_first_bad(n, first_bad):
    assert first_bad_version(n, lambda v: v >= first_bad) == first_bad

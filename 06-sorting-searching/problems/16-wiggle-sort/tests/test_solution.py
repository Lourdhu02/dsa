import pytest
from solution import wiggle_sort


def _is_wiggle(a):
    for i in range(len(a) - 1):
        if i % 2 == 0:
            if not a[i] <= a[i + 1]:
                return False
        else:
            if not a[i] >= a[i + 1]:
                return False
    return True


@pytest.mark.parametrize(
    "given",
    [[3, 5, 2, 1, 6, 4], [1, 2, 3, 4], [4, 1, 3, 2], [1], []],
)
def test_examples(given):
    a = given[:]
    wiggle_sort(a)
    assert _is_wiggle(a)

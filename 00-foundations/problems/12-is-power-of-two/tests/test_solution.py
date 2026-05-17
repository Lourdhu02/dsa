import pytest

from solution import is_power_of_two


@pytest.mark.parametrize(
    "n, expected",
    [(1, True), (2, True), (16, True), (1024, True), (3, False), (0, False), (-2, False), (2**40, True)],
)
def test_examples(n, expected):
    assert is_power_of_two(n) == expected


def test_first_30_powers():
    for k in range(30):
        assert is_power_of_two(1 << k)


def test_non_powers_up_to_100():
    powers = {1 << k for k in range(20)}
    for n in range(1, 100):
        assert is_power_of_two(n) == (n in powers)

import pytest

from solution import reverse_integer


@pytest.mark.parametrize(
    "n, expected",
    [(123, 321), (-456, -654), (1200, 21), (0, 0), (1_000_000_003, 3_000_000_001), (-100, -1)],
)
def test_examples(n, expected):
    assert reverse_integer(n) == expected


def test_double_reverse_is_identity_mod_trailing_zeros():
    for n in (123, 4567, -890, 10001):
        # Reversing twice strips leading zeros once, so we strip from the original first.
        original = int(str(abs(n)).rstrip("0")) * (-1 if n < 0 else 1)
        assert reverse_integer(reverse_integer(n)) == original

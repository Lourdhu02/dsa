import pytest

from solution import reverse_bits_32


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1 << 31),
        (43261596, 964176192),
        (2**32 - 1, 2**32 - 1),
        (4294967293, 3221225471),
    ],
)
def test_examples(n, expected):
    assert reverse_bits_32(n) == expected


def test_double_reverse_is_identity():
    for n in (0, 1, 7, 12345, 2**16, 2**31, 2**32 - 1):
        assert reverse_bits_32(reverse_bits_32(n)) == n


def test_out_of_range_raises():
    with pytest.raises(ValueError):
        reverse_bits_32(-1)
    with pytest.raises(ValueError):
        reverse_bits_32(1 << 32)

import pytest

from solution import get_hint


@pytest.mark.parametrize(
    "secret, guess, expected",
    [
        ("1807", "7810", "1A3B"),
        ("1123", "0111", "1A1B"),
        ("1", "0", "0A0B"),
        ("1", "1", "1A0B"),
    ],
)
def test_examples(secret, guess, expected):
    assert get_hint(secret, guess) == expected

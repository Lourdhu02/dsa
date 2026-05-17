import pytest

from solution import is_valid


@pytest.mark.parametrize(
    "s, expected",
    [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("", True), ("{[]}", True)],
)
def test_examples(s, expected):
    assert is_valid(s) is expected

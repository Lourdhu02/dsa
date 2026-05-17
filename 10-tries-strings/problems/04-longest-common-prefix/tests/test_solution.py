import pytest
from solution import longest_common_prefix


@pytest.mark.parametrize(
    "strs, expected",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""), ([""], ""), (["a"], "a")],
)
def test_examples(strs, expected):
    assert longest_common_prefix(strs) == expected

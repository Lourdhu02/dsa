import pytest

from solution import exclusive_time


@pytest.mark.parametrize(
    "n, logs, expected",
    [
        (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"], [3, 4]),
        (1, ["0:start:0", "0:start:2", "0:end:5", "0:end:6"], [7]),
    ],
)
def test_examples(n, logs, expected):
    assert exclusive_time(n, logs) == expected

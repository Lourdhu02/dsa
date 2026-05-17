import pytest
from solution import equations_possible


@pytest.mark.parametrize(
    "eqs, expected",
    [
        (["a==b", "b!=a"], False),
        (["a==b", "b==c", "a==c"], True),
        (["a!=a"], False),
        (["b==a", "a==b"], True),
    ],
)
def test_examples(eqs, expected):
    assert equations_possible(eqs) is expected

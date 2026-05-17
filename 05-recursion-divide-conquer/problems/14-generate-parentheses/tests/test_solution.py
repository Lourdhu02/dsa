import pytest

from solution import generate_parenthesis


def test_n3():
    assert sorted(generate_parenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )


def test_n1():
    assert generate_parenthesis(1) == ["()"]


def test_n0_count():
    assert generate_parenthesis(0) == [""]

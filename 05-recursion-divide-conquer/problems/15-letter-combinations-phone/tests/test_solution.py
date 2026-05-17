import pytest

from solution import letter_combinations


def test_two_digits():
    assert sorted(letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )


def test_empty():
    assert letter_combinations("") == []


def test_one_digit():
    assert sorted(letter_combinations("2")) == ["a", "b", "c"]

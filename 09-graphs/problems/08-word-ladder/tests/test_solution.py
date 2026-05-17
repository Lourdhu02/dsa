import pytest
from solution import ladder_length


def test_reachable():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5


def test_unreachable():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0

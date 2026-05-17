"""Sanity tests on the operation-count helpers.

We don't time these (machine-dependent); we count operations and check the
formula matches the documented Θ-bound.
"""

import math

from solutions.growth import (
    constant_ops,
    linear_ops,
    log_ops,
    n_log_n_ops,
    quadratic_ops,
)


def test_constant_is_constant():
    assert constant_ops(1) == constant_ops(1_000_000)


def test_log_ops_matches_floor_log2():
    # log_ops halves n until 1, so it returns floor(log2(n)).
    for n in (1, 2, 3, 4, 7, 8, 15, 16, 1024):
        assert log_ops(n) == math.floor(math.log2(n))


def test_linear_ops_is_n():
    for n in (0, 1, 10, 1_000):
        assert linear_ops(n) == n


def test_n_log_n_ops_matches_formula():
    # The inner loop runs floor(log2(max(n,1))) times for each of n outer iters.
    for n in (1, 2, 10, 64):
        expected = n * math.floor(math.log2(max(n, 1)))
        assert n_log_n_ops(n) == expected


def test_quadratic_ops_is_n_squared():
    for n in (0, 1, 5, 32):
        assert quadratic_ops(n) == n * n

"""Master-theorem case analysis tests.

These mirror the worked examples in the lesson README.
"""

from solutions.recurrences import master_theorem


def test_merge_sort_case_two():
    # T(n) = 2T(n/2) + Θ(n) — log_b a = 1, k = 1 → case 2.
    r = master_theorem(2, 2, 1)
    assert r.case == 2
    assert r.bound == "Theta(n^1 log n)"


def test_strassen_case_one():
    # T(n) = 7T(n/2) + Θ(n^2) — log_2 7 ≈ 2.807 > 2 → case 1.
    r = master_theorem(7, 2, 2)
    assert r.case == 1
    assert r.bound.startswith("Theta(n^2.807")


def test_case_three_when_f_dominates():
    # T(n) = 2T(n/2) + Θ(n^2) — log_b a = 1 < 2 → case 3.
    r = master_theorem(2, 2, 2)
    assert r.case == 3
    assert r.bound == "Theta(n^2)"


def test_validation():
    import pytest

    with pytest.raises(ValueError):
        master_theorem(0, 2, 1)
    with pytest.raises(ValueError):
        master_theorem(2, 1, 1)
    with pytest.raises(ValueError):
        master_theorem(2, 2, -1)

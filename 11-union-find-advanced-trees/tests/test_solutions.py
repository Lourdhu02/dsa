import random

from solutions.bit import BIT
from solutions.dsu import DSU
from solutions.segment_tree import SegmentTreeSum


def test_dsu_basic():
    d = DSU(5)
    assert d.count == 5
    assert d.union(0, 1)
    assert d.union(2, 3)
    assert not d.union(0, 1)
    assert d.connected(0, 1)
    assert not d.connected(0, 2)
    d.union(1, 3)
    assert d.connected(0, 3)
    assert d.count == 2


def test_segment_tree_random_against_brute_force():
    rng = random.Random(0)
    a = [rng.randint(-10, 10) for _ in range(50)]
    st = SegmentTreeSum(a)
    for _ in range(50):
        op = rng.choice(["update", "query"])
        if op == "update":
            i = rng.randrange(50)
            v = rng.randint(-10, 10)
            a[i] = v
            st.update(i, v)
        else:
            l = rng.randrange(50)
            r = rng.randrange(l, 50)
            assert st.range_sum(l, r) == sum(a[l : r + 1])


def test_bit_random_against_brute_force():
    rng = random.Random(1)
    n = 30
    a = [0] * (n + 1)
    bit = BIT(n)
    for _ in range(50):
        if rng.random() < 0.5:
            i = rng.randint(1, n)
            d = rng.randint(-5, 5)
            a[i] += d
            bit.update(i, d)
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            assert bit.range_sum(l, r) == sum(a[l : r + 1])

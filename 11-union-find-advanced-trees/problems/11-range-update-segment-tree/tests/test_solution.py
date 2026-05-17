import random
from solution import RangeUpdateSum


def test_basic():
    ru = RangeUpdateSum([1, 1, 1, 1])
    ru.range_add(0, 2, 5)
    assert ru.range_sum(0, 3) == 19
    assert ru.range_sum(0, 0) == 6
    assert ru.range_sum(3, 3) == 1


def test_random_against_brute():
    rng = random.Random(0)
    n = 30
    a = [rng.randint(-5, 5) for _ in range(n)]
    ru = RangeUpdateSum(a)
    for _ in range(50):
        op = rng.choice(["add", "query"])
        l = rng.randrange(n); r = rng.randrange(l, n)
        if op == "add":
            d = rng.randint(-3, 3)
            for i in range(l, r + 1):
                a[i] += d
            ru.range_add(l, r, d)
        else:
            assert ru.range_sum(l, r) == sum(a[l : r + 1])

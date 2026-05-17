import random

from solutions.heap import MinHeap


def test_push_then_pop_yields_sorted():
    h = MinHeap()
    xs = [5, 2, 8, 1, 4, 9, 3]
    for x in xs:
        h.push(x)
    out = []
    while len(h) > 0:
        out.append(h.pop())
    assert out == sorted(xs)


def test_heapify_then_pop_yields_sorted():
    rng = random.Random(7)
    xs = [rng.randint(-100, 100) for _ in range(200)]
    h = MinHeap(xs)
    out = []
    while len(h) > 0:
        out.append(h.pop())
    assert out == sorted(xs)


def test_peek_is_min():
    h = MinHeap([3, 1, 4, 1, 5])
    assert h.peek() == 1

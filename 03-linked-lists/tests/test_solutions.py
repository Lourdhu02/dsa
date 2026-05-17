from solutions.lru import LRUCache
from solutions.singly import from_iterable, reverse, to_list


def test_from_iterable_and_to_list_roundtrip():
    assert to_list(from_iterable([])) == []
    assert to_list(from_iterable([1, 2, 3])) == [1, 2, 3]


def test_reverse_basic():
    head = from_iterable([1, 2, 3, 4, 5])
    assert to_list(reverse(head)) == [5, 4, 3, 2, 1]


def test_reverse_empty_and_single():
    assert reverse(None) is None
    assert to_list(reverse(from_iterable([7]))) == [7]


def test_lru_basic_get_put():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)  # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)  # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


def test_lru_update_does_not_evict():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 100)
    assert c.get(1) == 100
    assert c.get(2) == 2

from solution import MyHashSet


def test_basic_flow():
    s = MyHashSet()
    s.add(1)
    s.add(2)
    assert s.contains(1)
    assert not s.contains(3)
    s.remove(2)
    assert not s.contains(2)


def test_idempotent_add():
    s = MyHashSet()
    for _ in range(10):
        s.add(5)
    assert s.contains(5)

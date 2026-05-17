from solution import MyHashMap


def test_basic_flow():
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1
    m.put(2, 1)
    assert m.get(2) == 1
    m.remove(2)
    assert m.get(2) == -1


def test_many_inserts_with_resize():
    m = MyHashMap()
    for i in range(200):
        m.put(i, i * 10)
    for i in range(200):
        assert m.get(i) == i * 10


def test_update_does_not_grow():
    m = MyHashMap()
    for _ in range(100):
        m.put(7, 1)
    assert m.get(7) == 1

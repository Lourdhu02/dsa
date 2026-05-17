from solutions.hash_table import HashMapChaining, HashSetOpenAddressing


def test_chaining_basic_crud():
    m = HashMapChaining()
    m["a"] = 1
    m["b"] = 2
    assert len(m) == 2
    assert m["a"] == 1
    m["a"] = 10
    assert m["a"] == 10
    assert "b" in m
    del m["a"]
    assert "a" not in m
    assert len(m) == 1


def test_chaining_resize_keeps_data():
    m = HashMapChaining()
    for i in range(100):
        m[i] = i * i
    assert len(m) == 100
    for i in range(100):
        assert m[i] == i * i


def test_chaining_missing_key():
    import pytest

    m = HashMapChaining()
    with pytest.raises(KeyError):
        _ = m["missing"]


def test_open_addressing_basic():
    s = HashSetOpenAddressing()
    for i in range(50):
        s.add(i)
    assert len(s) == 50
    for i in range(50):
        assert i in s
    s.remove(10)
    assert 10 not in s
    assert len(s) == 49


def test_open_addressing_tombstone_reuse():
    s = HashSetOpenAddressing()
    s.add("a")
    s.remove("a")
    s.add("a")
    assert "a" in s
    assert len(s) == 1

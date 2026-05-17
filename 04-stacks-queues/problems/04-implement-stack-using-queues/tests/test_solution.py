from solution import MyStack


def test_classic_flow():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()
    assert s.pop() == 1
    assert s.empty()

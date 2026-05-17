from solution import MyQueue


def test_classic_flow():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()
    assert q.pop() == 2
    assert q.empty()

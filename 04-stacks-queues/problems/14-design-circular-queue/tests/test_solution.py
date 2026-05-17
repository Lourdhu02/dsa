from solution import MyCircularQueue


def test_classic_flow():
    q = MyCircularQueue(3)
    assert q.en_queue(1)
    assert q.en_queue(2)
    assert q.en_queue(3)
    assert not q.en_queue(4)
    assert q.rear() == 3
    assert q.is_full()
    assert q.de_queue()
    assert q.en_queue(4)
    assert q.rear() == 4


def test_empty_returns_minus_one():
    q = MyCircularQueue(2)
    assert q.front() == -1
    assert q.rear() == -1

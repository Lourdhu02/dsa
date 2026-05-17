from solution import MinStack


def test_classic_flow():
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2


def test_repeated_min():
    ms = MinStack()
    ms.push(2)
    ms.push(2)
    ms.push(1)
    assert ms.get_min() == 1
    ms.pop()
    assert ms.get_min() == 2
    ms.pop()
    assert ms.get_min() == 2

from solution import Node, clone_graph


def test_small_graph():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.neighbors = [b, d]
    b.neighbors = [a, c]
    c.neighbors = [b, d]
    d.neighbors = [a, c]
    copy = clone_graph(a)
    assert copy is not a
    assert copy.val == 1
    assert {n.val for n in copy.neighbors} == {2, 4}


def test_none():
    assert clone_graph(None) is None

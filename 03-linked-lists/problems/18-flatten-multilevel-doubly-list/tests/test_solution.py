from solution import Node, flatten


def _build_simple_flat(values):
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0] if nodes else None


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_no_children():
    head = _build_simple_flat([1, 2, 3])
    assert _to_list(flatten(head)) == [1, 2, 3]


def test_one_level_child():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    d = Node(4)
    e = Node(5)
    d.next = e
    e.prev = d
    b.child = d
    assert _to_list(flatten(a)) == [1, 2, 4, 5, 3]


def test_empty():
    assert flatten(None) is None

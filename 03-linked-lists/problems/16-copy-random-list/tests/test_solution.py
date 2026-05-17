from solution import Node, copy_random_list


def _build(values, random_idx):
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, r in enumerate(random_idx):
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def _serialize(head):
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [(n.val, index.get(id(n.random))) for n in nodes]


def test_basic_copy():
    head = _build([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copy = copy_random_list(head)
    assert copy is not head
    assert _serialize(copy) == _serialize(head)


def test_empty():
    assert copy_random_list(None) is None

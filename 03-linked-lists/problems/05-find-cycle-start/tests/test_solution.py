from solution import ListNode, detect_cycle


def _build(xs, pos):
    if not xs:
        return None, None
    nodes = [ListNode(v) for v in xs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    cycle_node = None
    if pos >= 0:
        nodes[-1].next = nodes[pos]
        cycle_node = nodes[pos]
    return nodes[0], cycle_node


def test_no_cycle():
    head, _ = _build([1, 2, 3], -1)
    assert detect_cycle(head) is None


def test_cycle_in_middle():
    head, cycle_node = _build([3, 2, 0, -4], 1)
    assert detect_cycle(head) is cycle_node


def test_self_loop():
    head, cycle_node = _build([1], 0)
    assert detect_cycle(head) is cycle_node


def test_empty():
    assert detect_cycle(None) is None

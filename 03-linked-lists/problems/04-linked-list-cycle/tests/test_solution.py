from solution import ListNode, has_cycle


def _build_with_cycle(xs, pos):
    if not xs:
        return None
    nodes = [ListNode(v) for v in xs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test_no_cycle():
    assert has_cycle(_build_with_cycle([1, 2, 3, 4, 5], -1)) is False


def test_cycle_at_head():
    assert has_cycle(_build_with_cycle([1, 2, 3], 0)) is True


def test_cycle_in_middle():
    assert has_cycle(_build_with_cycle([1, 2, 3, 4, 5], 2)) is True


def test_empty():
    assert has_cycle(None) is False

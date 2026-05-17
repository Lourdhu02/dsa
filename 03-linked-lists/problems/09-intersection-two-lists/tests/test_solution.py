from solution import ListNode, get_intersection


def _link(values_before, shared_values, prefix_to_share=True):
    shared = None
    for v in reversed(shared_values):
        shared = ListNode(v, shared)
    head = shared
    for v in reversed(values_before):
        head = ListNode(v, head)
    return head, shared


def test_intersect_in_middle():
    shared_values = [8, 4, 5]
    a_head, shared = _link([4, 1], shared_values)
    b_head, _ = _link([5, 6, 1], [])
    # rebuild b with the shared tail
    cur = b_head
    while cur.next is not None:
        cur = cur.next
    cur.next = shared
    assert get_intersection(a_head, b_head) is shared


def test_no_intersection():
    a = ListNode(1, ListNode(2))
    b = ListNode(3, ListNode(4))
    assert get_intersection(a, b) is None


def test_both_none():
    assert get_intersection(None, None) is None

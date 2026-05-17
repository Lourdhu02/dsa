from solution import ListNode, merge_k_lists


def _build(xs):
    head = None
    for v in reversed(xs):
        head = ListNode(v, head)
    return head


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_basic():
    lists = [_build([1, 4, 5]), _build([1, 3, 4]), _build([2, 6])]
    assert _to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_empty_lists():
    assert merge_k_lists([]) is None
    assert merge_k_lists([None, None]) is None

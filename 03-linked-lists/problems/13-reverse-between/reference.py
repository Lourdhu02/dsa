class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    if head is None or left == right:
        return head
    sentinel = ListNode(0, head)
    prev = sentinel
    for _ in range(left - 1):
        assert prev.next is not None
        prev = prev.next
    cur = prev.next
    assert cur is not None
    # In-place: move cur.next to position prev.next.
    for _ in range(right - left):
        nxt = cur.next
        assert nxt is not None
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return sentinel.next

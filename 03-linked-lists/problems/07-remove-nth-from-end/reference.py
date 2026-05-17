class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """One pass with offset fast/slow pointers.

    Time: Θ(L).  Space: Θ(1).
    """
    sentinel = ListNode(0, head)
    fast: ListNode | None = sentinel
    slow: ListNode = sentinel
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next  # type: ignore[assignment]
    if slow.next is not None:
        slow.next = slow.next.next
    return sentinel.next

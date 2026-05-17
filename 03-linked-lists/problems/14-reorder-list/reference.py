class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reorder_list(head: ListNode | None) -> None:
    if head is None or head.next is None:
        return
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    second = slow.next  # type: ignore[union-attr]
    slow.next = None  # type: ignore[union-attr]
    prev = None
    curr = second
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev
    p1, p2 = head, second
    while p2 is not None:
        n1, n2 = p1.next, p2.next  # type: ignore[union-attr]
        p1.next = p2  # type: ignore[union-attr]
        p2.next = n1
        p1 = n1
        p2 = n2

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def _reverse(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def is_palindrome(head: ListNode | None) -> bool:
    """Time: Θ(n).  Space: Θ(1)."""
    if head is None or head.next is None:
        return True
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    second = _reverse(slow.next)  # type: ignore[union-attr]
    p1, p2 = head, second
    ok = True
    while p2 is not None:
        if p1.val != p2.val:
            ok = False
            break
        p1 = p1.next  # type: ignore[union-attr]
        p2 = p2.next
    return ok

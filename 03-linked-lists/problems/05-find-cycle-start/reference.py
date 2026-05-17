class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def detect_cycle(head: ListNode | None) -> ListNode | None:
    """Floyd cycle-find with phase-2 entry locator.

    Time:  Θ(n).  Space: Θ(1).
    Proof: see lesson README §2.
    """
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p = p.next  # type: ignore[union-attr]
                slow = slow.next  # type: ignore[union-attr]
            return p
    return None

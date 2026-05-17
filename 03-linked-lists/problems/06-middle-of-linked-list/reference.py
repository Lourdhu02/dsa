class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def middle_node(head: ListNode | None) -> ListNode | None:
    """Time: Θ(n).  Space: Θ(1)."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    return slow

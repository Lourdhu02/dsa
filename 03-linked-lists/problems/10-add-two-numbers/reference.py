class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Time: Θ(max(n, m)).  Space: Θ(max(n, m))."""
    sentinel = ListNode()
    tail = sentinel
    carry = 0
    while a is not None or b is not None or carry:
        x = a.val if a is not None else 0
        y = b.val if b is not None else 0
        s = x + y + carry
        carry, digit = divmod(s, 10)
        tail.next = ListNode(digit)
        tail = tail.next
        a = a.next if a is not None else None
        b = b.next if b is not None else None
    return sentinel.next

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build(xs: list[int]) -> ListNode | None:
    """Time: Θ(n).  Space: Θ(n)."""
    head: ListNode | None = None
    tail: ListNode | None = None
    for v in xs:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def to_list(head: ListNode | None) -> list[int]:
    """Time: Θ(n).  Space: Θ(n) for the output."""
    out: list[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out

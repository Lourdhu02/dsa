class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None or k == 0:
        return head
    n = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    tail.next = head
    steps = n - k
    new_tail = head
    for _ in range(steps - 1):
        assert new_tail.next is not None
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def get_intersection(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    if a is None or b is None:
        return None
    p1, p2 = a, b
    while p1 is not p2:
        p1 = p1.next if p1 is not None else b
        p2 = p2.next if p2 is not None else a
    return p1

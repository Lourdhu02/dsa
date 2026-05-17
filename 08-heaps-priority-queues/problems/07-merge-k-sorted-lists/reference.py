import heapq


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """Time: Θ(N log k).  Space: Θ(k)."""
    h: list[tuple[int, int, ListNode]] = []
    for i, head in enumerate(lists):
        if head is not None:
            heapq.heappush(h, (head.val, i, head))
    sentinel = ListNode()
    tail = sentinel
    while h:
        val, i, node = heapq.heappop(h)
        tail.next = node
        tail = node
        if node.next is not None:
            heapq.heappush(h, (node.next.val, i, node.next))
    tail.next = None
    return sentinel.next

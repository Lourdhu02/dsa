class Node:
    def __init__(self, val: int = 0, prev: "Node | None" = None, next: "Node | None" = None, child: "Node | None" = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Node | None) -> Node | None:
    if head is None:
        return None
    stack: list[Node] = []
    cur = head
    while cur is not None:
        if cur.child is not None:
            if cur.next is not None:
                stack.append(cur.next)
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
        if cur.next is None and stack:
            nxt = stack.pop()
            cur.next = nxt
            nxt.prev = cur
        cur = cur.next
    return head

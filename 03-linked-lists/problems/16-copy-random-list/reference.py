class Node:
    def __init__(self, val: int = 0, next: "Node | None" = None, random: "Node | None" = None) -> None:
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node | None) -> Node | None:
    """Time: Θ(n).  Space: Θ(n)."""
    if head is None:
        return None
    mapping: dict[int, Node] = {}
    cur: Node | None = head
    while cur is not None:
        mapping[id(cur)] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur is not None:
        clone = mapping[id(cur)]
        clone.next = mapping[id(cur.next)] if cur.next is not None else None
        clone.random = mapping[id(cur.random)] if cur.random is not None else None
        cur = cur.next
    return mapping[id(head)]

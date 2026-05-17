class Node:
    def __init__(self, val: int = 0, prev: "Node | None" = None, next: "Node | None" = None, child: "Node | None" = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Node | None) -> Node | None:
    # TODO
    raise NotImplementedError

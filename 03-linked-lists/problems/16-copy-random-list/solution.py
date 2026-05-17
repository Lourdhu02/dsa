class Node:
    def __init__(self, val: int = 0, next: "Node | None" = None, random: "Node | None" = None) -> None:
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node | None) -> Node | None:
    # TODO
    raise NotImplementedError

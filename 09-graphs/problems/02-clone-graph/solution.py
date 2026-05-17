class Node:
    def __init__(self, val: int = 0, neighbors: "list[Node] | None" = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    # TODO
    raise NotImplementedError

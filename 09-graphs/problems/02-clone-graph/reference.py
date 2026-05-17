class Node:
    def __init__(self, val: int = 0, neighbors: "list[Node] | None" = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    if node is None:
        return None
    mapping: dict[int, Node] = {}

    def _clone(u: Node) -> Node:
        if id(u) in mapping:
            return mapping[id(u)]
        copy = Node(u.val)
        mapping[id(u)] = copy
        copy.neighbors = [_clone(v) for v in u.neighbors]
        return copy

    return _clone(node)

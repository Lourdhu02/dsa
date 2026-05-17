class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    out: list[int] = []
    layer = [root]
    while layer:
        out.append(layer[-1].val)
        nxt = []
        for n in layer:
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        layer = nxt
    return out

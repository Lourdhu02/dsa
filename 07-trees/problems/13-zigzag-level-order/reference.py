class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def zigzag(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    out: list[list[int]] = []
    layer = [root]
    rev = False
    while layer:
        vals = [n.val for n in layer]
        out.append(list(reversed(vals)) if rev else vals)
        rev = not rev
        nxt = []
        for n in layer:
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        layer = nxt
    return out

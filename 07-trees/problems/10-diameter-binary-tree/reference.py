class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def diameter(root: TreeNode | None) -> int:
    best = 0

    def _h(node):
        nonlocal best
        if node is None:
            return 0
        lh = _h(node.left)
        rh = _h(node.right)
        best = max(best, lh + rh)
        return 1 + max(lh, rh)

    _h(root)
    return best

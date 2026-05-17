class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca_bst(root: TreeNode | None, p: int, q: int) -> TreeNode | None:
    lo, hi = min(p, q), max(p, q)
    cur = root
    while cur is not None:
        if cur.val < lo:
            cur = cur.right
        elif cur.val > hi:
            cur = cur.left
        else:
            return cur
    return None

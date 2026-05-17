class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """Time: Θ(n).  Space: Θ(n)."""
    idx = {v: i for i, v in enumerate(inorder)}
    pre_iter = iter(preorder)

    def _rec(lo: int, hi: int):
        if lo > hi:
            return None
        root_val = next(pre_iter)
        node = TreeNode(root_val)
        i = idx[root_val]
        node.left = _rec(lo, i - 1)
        node.right = _rec(i + 1, hi)
        return node

    return _rec(0, len(inorder) - 1)

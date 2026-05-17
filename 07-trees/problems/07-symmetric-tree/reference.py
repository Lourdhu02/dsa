class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    def _mirror(a, b):
        if a is None or b is None:
            return a is b
        return a.val == b.val and _mirror(a.left, b.right) and _mirror(a.right, b.left)

    return root is None or _mirror(root.left, root.right)

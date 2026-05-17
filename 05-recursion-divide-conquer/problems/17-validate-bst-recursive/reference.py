class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def _rec(node, low, high):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return _rec(node.left, low, node.val) and _rec(node.right, node.val, high)

    return _rec(root, float("-inf"), float("inf"))

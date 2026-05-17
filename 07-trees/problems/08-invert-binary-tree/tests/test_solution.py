from solution import TreeNode, invert_tree


def _level_order(root):
    if root is None:
        return []
    out, q = [], [root]
    while q:
        nxt = []
        for n in q:
            out.append(n.val)
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        q = nxt
    return out


def test_basic():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(root)
    assert _level_order(inverted) == [4, 7, 2, 9, 6, 3, 1]


def test_empty():
    assert invert_tree(None) is None

from solution import TreeNode, build_tree


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.val] + _inorder(node.right)


def _preorder(node):
    if node is None:
        return []
    return [node.val] + _preorder(node.left) + _preorder(node.right)


def test_classic():
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    root = build_tree(pre, ino)
    assert _preorder(root) == pre
    assert _inorder(root) == ino


def test_empty():
    assert build_tree([], []) is None


def test_single_node():
    root = build_tree([1], [1])
    assert root is not None and root.val == 1

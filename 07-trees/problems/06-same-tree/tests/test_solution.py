from solution import TreeNode, is_same_tree


def test_same():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) is True


def test_different():
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) is False


def test_both_empty():
    assert is_same_tree(None, None) is True

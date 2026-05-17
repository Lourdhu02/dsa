from solution import TreeNode, is_balanced


def test_balanced():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(root) is True


def test_unbalanced():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert is_balanced(root) is False


def test_empty():
    assert is_balanced(None) is True

from solution import TreeNode, is_valid_bst


def test_valid_simple():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) is True


def test_invalid_right_subtree():
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root) is False


def test_equal_values_invalid():
    root = TreeNode(2, TreeNode(2))
    assert is_valid_bst(root) is False


def test_empty():
    assert is_valid_bst(None) is True

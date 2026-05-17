from solution import TreeNode, has_path_sum


def test_present():
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert has_path_sum(root, 22) is True


def test_absent():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert has_path_sum(root, 5) is False


def test_empty():
    assert has_path_sum(None, 0) is False

from solution import TreeNode, lca_bst


def test_basic():
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    assert lca_bst(root, 2, 8).val == 6
    assert lca_bst(root, 2, 4).val == 2
    assert lca_bst(root, 3, 5).val == 4

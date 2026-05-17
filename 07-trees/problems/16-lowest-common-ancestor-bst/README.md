# 16. LCA in BST  `[medium]`

Find the lowest common ancestor of nodes with values `p` and `q` in a BST. Both values exist in the tree.

## Function signature

```python
def lca_bst(root: TreeNode | None, p: int, q: int) -> TreeNode | None: ...
```

## Examples

In `[6,2,8,0,4,7,9,None,None,3,5]`, LCA(2, 8) = 6. LCA(2, 4) = 2.



## Hint

<details>
<summary>Hint</summary>

Walk from the root. If both `p, q` are less than `root.val`, go left. If both greater, go right. Else split point — return root.
</details>

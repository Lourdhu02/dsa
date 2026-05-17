# 17. LCA in binary tree  `[medium]`

Find the lowest common ancestor of nodes `p` and `q` in a binary tree (NOT a BST). Both nodes exist.

## Function signature

```python
def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None: ...
```

## Examples

In `[3,5,1,6,2,0,8,None,None,7,4]`, LCA(5, 1) = 3.



## Hint

<details>
<summary>Hint</summary>

Recurse. Return p/q on match; null on miss. If both subtrees return non-null, this node is the LCA. Otherwise propagate whichever child returned non-null.
</details>

# 18. Construct tree from preorder + inorder  `[medium]`

Given preorder and inorder traversal arrays of a binary tree (all values distinct), reconstruct the tree and return its root.

## Function signature

```python
class TreeNode: ...

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None: ...
```

## Examples

```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

result:
        3
       / \
      9  20
        /  \
       15   7
```



## Hint

<details>
<summary>Hint</summary>

First element of preorder is the root. Find it in inorder to split left/right subtree ranges, then recurse. Index inorder values in a hash map for `Θ(1)` lookup so the total is `Θ(n)`.
</details>

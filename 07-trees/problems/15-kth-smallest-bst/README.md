# 15. Kth smallest in BST  `[medium]`

Return the kth smallest value (1-indexed) in a BST.

## Function signature

```python
def kth_smallest(root: TreeNode | None, k: int) -> int: ...
```

## Examples

`[3, 1, 4, None, 2]`, k=1 → 1. k=3 → 3.



## Hint

<details>
<summary>Hint</summary>

Inorder traversal yields sorted order; stop at the kth element.
</details>

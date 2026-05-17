# 14. Validate BST  `[medium]`

Return True if a binary tree is a valid BST (strict: left < node < right for every node).

## Function signature

```python
def is_valid_bst(root: TreeNode | None) -> bool: ...
```

## Examples

`[2, 1, 3]` → True.
`[5, 1, 4, None, None, 3, 6]` → False (3 sits in 5's right subtree).



## Hint

<details>
<summary>Hint</summary>

Recurse with `(low, high)` bounds.
</details>

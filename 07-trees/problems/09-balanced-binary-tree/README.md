# 09. Balanced binary tree  `[easy]`

Return True if for every node, the heights of its two subtrees differ by at most 1.

## Function signature

```python
def is_balanced(root: TreeNode | None) -> bool: ...
```

## Examples

`[3, 9, 20, None, None, 15, 7]` is balanced.
`[1, 2, 2, 3, 3, None, None, 4, 4]` is not.



## Hint

<details>
<summary>Hint</summary>

Bottom-up: each call returns the height OR -1 if unbalanced. Propagate -1 up.
</details>

# 05. Maximum depth of binary tree  `[easy]`

Return the maximum depth of a binary tree (number of nodes on longest root-to-leaf path).

## Function signature

```python
def max_depth(root: TreeNode | None) -> int: ...
```

## Examples

| tree | depth |
|---|---|
| `[3, 9, 20, None, None, 15, 7]` | 3 |
| `[]` | 0 |



## Hint

<details>
<summary>Hint</summary>

`max_depth(None) == 0; else 1 + max(left, right)`.
</details>

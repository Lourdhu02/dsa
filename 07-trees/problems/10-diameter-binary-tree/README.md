# 10. Diameter of binary tree  `[easy]`

Return the length (number of edges) of the longest path between any two nodes. The path may or may not pass through the root.

## Function signature

```python
def diameter(root: TreeNode | None) -> int: ...
```

## Examples

| tree | diameter |
|---|---|
| `[1, 2, 3, 4, 5]` | 3 (path 4-2-1-3 or 5-2-1-3) |
| `[1, 2]` | 1 |



## Hint

<details>
<summary>Hint</summary>

Bottom-up. Each node returns its height; the diameter through that node is `left_height + right_height`. Track max.
</details>

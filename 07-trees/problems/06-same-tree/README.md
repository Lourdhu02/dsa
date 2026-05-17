# 06. Same tree  `[easy]`

Return True if two binary trees are structurally identical and have equal values.

## Function signature

```python
def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool: ...
```

## Examples

| p | q | same |
|---|---|---|
| `[1, 2, 3]` | `[1, 2, 3]` | True |
| `[1, 2]` | `[1, None, 2]` | False |



## Hint

<details>
<summary>Hint</summary>

Recurse: both null → True; one null → False; values differ → False; else recurse on children.
</details>

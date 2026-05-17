# 11. Path sum (root to leaf)  `[easy]`

Return True if there is a root-to-leaf path with values summing to `target`.

## Function signature

```python
def has_path_sum(root: TreeNode | None, target: int) -> bool: ...
```

## Examples

```
target=22
tree=[5,4,8,11,null,13,4,7,2,null,null,null,1]   -> True (5+4+11+2)
```



## Hint

<details>
<summary>Hint</summary>

Recurse subtracting. At a leaf check if remaining == 0.
</details>

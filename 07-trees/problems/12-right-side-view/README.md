# 12. Binary tree right-side view  `[medium]`

Return the values visible when looking at the tree from the right side, top to bottom.

## Function signature

```python
def right_side_view(root: TreeNode | None) -> list[int]: ...
```

## Examples

```
   1
  / \
 2   3
  \   \
   5   4
```

Result: `[1, 3, 4]`.



## Hint

<details>
<summary>Hint</summary>

Level-order BFS; take the last node of each level.
</details>

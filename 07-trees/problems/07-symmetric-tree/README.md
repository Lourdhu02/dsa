# 07. Symmetric tree  `[easy]`

Return True if the binary tree is mirror-symmetric about its center.

## Function signature

```python
def is_symmetric(root: TreeNode | None) -> bool: ...
```

## Examples

```
    1
   / \
  2   2
 / \ / \
3  4 4  3        symmetric
```



## Hint

<details>
<summary>Hint</summary>

Helper compares `(left, right)`: same val AND mirror children.
</details>

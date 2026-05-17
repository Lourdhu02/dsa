# 01. Assign cookies  `[easy]`

Children have greed factors `g`. Cookies have sizes `s`. Each child gets at most one cookie that satisfies `s[i] >= g[j]`. Return the max number of satisfied children.

## Function signature

```python
def find_content_children(g: list[int], s: list[int]) -> int: ...
```

## Examples

| g | s | result |
|---|---|---|
| `[1, 2, 3]` | `[1, 1]` | 1 |
| `[1, 2]` | `[1, 2, 3]` | 2 |



## Hint

<details>
<summary>Hint</summary>

Sort both. Two pointers: assign smallest cookie that fits the smallest unsatisfied child.
</details>

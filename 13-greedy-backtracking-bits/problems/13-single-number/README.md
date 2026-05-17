# 13. Single number (XOR)  `[easy]`

Every element appears twice except one. Return that one. `Θ(n)` time, `Θ(1)` space.

## Function signature

```python
def single_number(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 2, 1]` | 1 |
| `[4, 1, 2, 1, 2]` | 4 |



## Hint

<details>
<summary>Hint</summary>

XOR all elements. Pairs cancel.
</details>

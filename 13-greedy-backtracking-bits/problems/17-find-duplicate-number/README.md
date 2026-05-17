# 17. Find the duplicate number (Floyd cycle)  `[medium]`

Given an array of `n + 1` integers each in `[1, n]` with exactly one repeated value, find the duplicate. `Θ(n)` time, `Θ(1)` extra space (don't modify input).

## Function signature

```python
def find_duplicate(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[1, 3, 4, 2, 2]` | 2 |
| `[3, 1, 3, 4, 2]` | 3 |



## Hint

<details>
<summary>Hint</summary>

Treat `nums[i]` as a pointer. There's a cycle. Floyd's tortoise/hare; the cycle entrance is the duplicate.
</details>

# 03. Jump game  `[medium]`

`nums[i]` is the max jump length from index i. Return True if you can reach the last index from index 0.

## Function signature

```python
def can_jump(nums: list[int]) -> bool: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 3, 1, 1, 4]` | True |
| `[3, 2, 1, 0, 4]` | False |



## Hint

<details>
<summary>Hint</summary>

Track furthest reachable. If i > furthest, fail. Update furthest = max(furthest, i + nums[i]).
</details>

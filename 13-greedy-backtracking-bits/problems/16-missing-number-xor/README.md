# 16. Missing number (XOR)  `[easy]`

Given `nums` containing `n` distinct numbers from `[0, n]`, return the one missing.

## Function signature

```python
def missing_number(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[3, 0, 1]` | 2 |
| `[0, 1]` | 2 |
| `[9, 6, 4, 2, 3, 5, 7, 0, 1]` | 8 |



## Hint

<details>
<summary>Hint</summary>

XOR all values in `nums` and all integers in `[0, n]`. Pairs cancel; the missing one survives.
</details>

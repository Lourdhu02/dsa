# 16. Maximum product subarray  `[medium]`

Return the largest product of any contiguous subarray.

## Function signature

```python
def max_product(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 3, -2, 4]` | 6 |
| `[-2, 0, -1]` | 0 |
| `[-2, 3, -4]` | 24 |



## Hint

<details>
<summary>Hint</summary>

Track both running max AND running min ending at i (a negative * negative_min becomes large positive).
</details>

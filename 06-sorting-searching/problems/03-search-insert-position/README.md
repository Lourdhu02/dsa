# 03. Search insert position  `[easy]`

Given a sorted array of distinct integers and a target, return the index where the target would be inserted to keep the array sorted.

## Function signature

```python
def search_insert(nums: list[int], target: int) -> int: ...
```

## Examples

| nums | target | result |
|---|---|---|
| `[1, 3, 5, 6]` | 5 | 2 |
| `[1, 3, 5, 6]` | 2 | 1 |
| `[1, 3, 5, 6]` | 7 | 4 |



## Hint

<details>
<summary>Hint</summary>

Lower bound: smallest index with `nums[i] >= target`.
</details>

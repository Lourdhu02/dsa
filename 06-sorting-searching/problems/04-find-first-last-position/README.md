# 04. Find first and last position  `[medium]`

Given a sorted array (with duplicates) and target, return `[first, last]` of target. `[-1, -1]` if absent.

## Function signature

```python
def search_range(nums: list[int], target: int) -> list[int]: ...
```

## Examples

| nums | target | result |
|---|---|---|
| `[5, 7, 7, 8, 8, 10]` | 8 | `[3, 4]` |
| `[5, 7, 7, 8, 8, 10]` | 6 | `[-1, -1]` |
| `[]` | 0 | `[-1, -1]` |



## Hint

<details>
<summary>Hint</summary>

Two binary searches: lower_bound(target) and upper_bound(target) - 1.
</details>

# 03. Remove duplicates from sorted array  `[easy]`

Given a sorted array, remove duplicates **in place** so each element appears once. Return the new length `k`. The first `k` slots of the array must hold the unique elements in their original order.

## Function signature

```python
def remove_duplicates(nums: list[int]) -> int: ...
```

## Examples

| input | k | first k elements |
|---|---|---|
| `[1, 1, 2]` | 2 | `[1, 2]` |
| `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` | 5 | `[0, 1, 2, 3, 4]` |
| `[]` | 0 | `[]` |
| `[7]` | 1 | `[7]` |

## Hint

<details>
<summary>Hint</summary>

Same-direction (fast/slow) two pointers. Slow points to the next write slot. Fast scans; copies a new value when it differs from `nums[slow-1]`.
</details>

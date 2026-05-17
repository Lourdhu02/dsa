# 10. Product of array except self  `[medium]`

Given an integer array `nums`, return an array `answer` such that `answer[i]` is the product of all elements of `nums` except `nums[i]`. Solve in `Θ(n)` time **without using division** (so it works when zeros appear).

## Function signature

```python
def product_except_self(nums: list[int]) -> list[int]: ...
```

## Examples

| nums | answer |
|---|---|
| `[1, 2, 3, 4]` | `[24, 12, 8, 6]` |
| `[-1, 1, 0, -3, 3]` | `[0, 0, 9, 0, 0]` |
| `[2, 3]` | `[3, 2]` |

## Hint

<details>
<summary>Hint</summary>

Two passes: build `left[i] = product of nums[:i]`, then walk right-to-left maintaining a running `right` product and set `answer[i] = left[i] * right`.
</details>

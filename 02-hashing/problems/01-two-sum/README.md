# 01. Two sum  `[easy]`

Given an integer array `nums` and an integer `target`, return the indices `(i, j)` (with `i < j`) of the two numbers such that `nums[i] + nums[j] == target`. Exactly one solution exists.

## Function signature

```python
def two_sum(nums: list[int], target: int) -> tuple[int, int]: ...
```

## Examples

| nums | target | result |
|---|---|---|
| `[2, 7, 11, 15]` | 9 | `(0, 1)` |
| `[3, 2, 4]` | 6 | `(1, 2)` |
| `[3, 3]` | 6 | `(0, 1)` |

## Constraints

- `2 <= len(nums) <= 10^4`


## Hint

<details>
<summary>Hint</summary>

One pass. For each `x`, check if `target - x` is already in a hash map of `value -> earliest index`. If yes, return the pair. If no, store `x` and continue.
</details>

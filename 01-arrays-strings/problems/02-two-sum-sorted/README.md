# 02. Two sum on sorted array  `[easy]`

Given a 1-indexed array of integers **sorted in non-decreasing order**, return the 1-indexed positions of two numbers that sum to `target`. Exactly one solution exists. You may not use the same element twice.

Sorted input unlocks the converging two-pointer pattern — Θ(n), no hash map needed (compare with module 02's hashed two-sum on the *unsorted* version).

## Function signature

```python
def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int]: ...
```

## Examples

| numbers | target | result |
|---|---|---|
| `[2, 7, 11, 15]` | 9 | `(1, 2)` |
| `[2, 3, 4]` | 6 | `(1, 3)` |
| `[-1, 0]` | -1 | `(1, 2)` |

## Constraints

- `2 <= len(numbers) <= 3 * 10^4`
- Numbers are sorted non-decreasing.

## Hint

<details>
<summary>Hint</summary>

Two pointers at the ends. If sum is too small, move left pointer right; if too big, move right pointer left.
</details>

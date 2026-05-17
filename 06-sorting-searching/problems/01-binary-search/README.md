# 01. Binary search  `[easy]`

Given a sorted array of distinct integers and a target, return the index of target or -1.

## Function signature

```python
def search(nums: list[int], target: int) -> int: ...
```

## Examples

| nums | target | result |
|---|---|---|
| `[-1, 0, 3, 5, 9, 12]` | 9 | 4 |
| `[-1, 0, 3, 5, 9, 12]` | 2 | -1 |

## Constraints

- `0 <= len(nums) <= 10^4`


## Hint

<details>
<summary>Hint</summary>

Standard closed-interval binary search. Pick one variant and stick to it.
</details>

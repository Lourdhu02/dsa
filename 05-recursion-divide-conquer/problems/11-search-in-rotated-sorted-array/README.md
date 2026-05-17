# 11. Search in rotated sorted array  `[medium]`

An array of distinct integers was sorted in ascending order then rotated at an unknown pivot. Given `nums` and `target`, return the index of `target` in `nums`, or `-1` if absent. `Θ(log n)` time.

## Function signature

```python
def search(nums: list[int], target: int) -> int: ...
```

## Examples

| nums | target | result |
|---|---|---|
| `[4, 5, 6, 7, 0, 1, 2]` | 0 | 4 |
| `[4, 5, 6, 7, 0, 1, 2]` | 3 | -1 |
| `[1]` | 0 | -1 |



## Hint

<details>
<summary>Hint</summary>

Modified binary search. At each step decide which half is sorted; check if target lies in that sorted half, otherwise recurse into the other.
</details>

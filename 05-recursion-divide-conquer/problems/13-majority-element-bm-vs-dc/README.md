# 13. Majority element (D&C variant)  `[medium]`

Find the element that appears more than `n/2` times in `nums` (it is guaranteed to exist). Solve with a divide-and-conquer approach (`Θ(n log n)`). The `Θ(n)` Boyer-Moore vote is shown in module 13.

## Function signature

```python
def majority_element(nums: list[int]) -> int: ...
```

## Examples

| nums | majority |
|---|---|
| `[3, 2, 3]` | 3 |
| `[2, 2, 1, 1, 1, 2, 2]` | 2 |



## Hint

<details>
<summary>Hint</summary>

Split the array. If both halves agree, that's the answer. Otherwise count occurrences of each candidate across the whole range.
</details>

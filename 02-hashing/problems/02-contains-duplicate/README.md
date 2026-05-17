# 02. Contains duplicate  `[easy]`

Return `True` if any value appears at least twice in the array, else `False`.

## Function signature

```python
def contains_duplicate(nums: list[int]) -> bool: ...
```

## Examples

| nums | result |
|---|---|
| `[1, 2, 3, 1]` | True |
| `[1, 2, 3, 4]` | False |
| `[]` | False |



## Hint

<details>
<summary>Hint</summary>

Walk the array, build a set; return True the moment you see a repeat. Alternative: `len(set(nums)) != len(nums)` — slightly slower because it always scans all of nums.
</details>

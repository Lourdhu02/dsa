# 05. Intersection of two arrays  `[easy]`

Given two integer arrays, return their set-style intersection: each element appears once, order doesn't matter.

## Function signature

```python
def intersection(a: list[int], b: list[int]) -> list[int]: ...
```

## Examples

| a | b | result (any order) |
|---|---|---|
| `[1, 2, 2, 1]` | `[2, 2]` | `[2]` |
| `[4, 9, 5]` | `[9, 4, 9, 8, 4]` | `[4, 9]` |



## Hint

<details>
<summary>Hint</summary>

Put `a` into a set; iterate `b`; collect items present in the set; deduplicate.
</details>

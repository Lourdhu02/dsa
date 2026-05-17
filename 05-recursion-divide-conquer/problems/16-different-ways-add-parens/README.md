# 16. Different ways to add parentheses  `[medium]`

Given an arithmetic expression of integers and `+`, `-`, `*`, return all possible results of inserting parentheses (any order of operations).

## Function signature

```python
def diff_ways_to_compute(expression: str) -> list[int]: ...
```

## Examples

| expression | results |
|---|---|
| `"2-1-1"` | `[0, 2]` |
| `"2*3-4*5"` | `[-34, -14, -10, -10, 10]` |



## Hint

<details>
<summary>Hint</summary>

Recurse on operators: split at each `+`, `-`, `*`; recursively compute results of left and right; combine pairwise.
</details>

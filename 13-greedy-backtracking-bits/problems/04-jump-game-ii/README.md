# 04. Jump game II (min jumps)  `[medium]`

Same input. Return the min number of jumps to reach the last index. Assume you can always reach it.

## Function signature

```python
def jump(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 3, 1, 1, 4]` | 2 |
| `[2, 3, 0, 1, 4]` | 2 |



## Hint

<details>
<summary>Hint</summary>

BFS-shaped greedy: maintain `current_end` and `farthest`. When `i == current_end`, increment jumps and set `current_end = farthest`.
</details>

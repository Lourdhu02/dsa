# 14. Minimum cost to connect ropes  `[easy]`

Connect `n` ropes into one. Connecting two ropes of lengths `a` and `b` costs `a + b`. Return the minimum total cost.

## Function signature

```python
def connect_ropes(ropes: list[int]) -> int: ...
```

## Examples

| ropes | cost |
|---|---|
| `[1, 2, 3, 4, 5]` | 33 |
| `[4, 3, 2, 6]` | 29 |



## Hint

<details>
<summary>Hint</summary>

Always connect the two shortest. Min-heap.
</details>

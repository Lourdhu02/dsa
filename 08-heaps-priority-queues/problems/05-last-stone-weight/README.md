# 05. Last stone weight  `[easy]`

Repeatedly take the two heaviest stones, smash them. If equal, both destroyed. Otherwise the difference replaces them. Return the weight of the last remaining stone, or 0 if none.

## Function signature

```python
def last_stone_weight(stones: list[int]) -> int: ...
```

## Examples

| stones | result |
|---|---|
| `[2, 7, 4, 1, 8, 1]` | 1 |
| `[1]` | 1 |
| `[3, 3]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Max-heap via negation.
</details>

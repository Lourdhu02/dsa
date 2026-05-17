# 06. Happy number  `[easy]`

A number is *happy* if repeatedly replacing it by the sum of squares of its digits eventually reaches 1. If it loops without reaching 1, it isn't happy. Return whether `n` is happy.

## Function signature

```python
def is_happy(n: int) -> bool: ...
```

## Examples

| n | result |
|---|---|
| 19 | True (`19 -> 82 -> 68 -> 100 -> 1`) |
| 2 | False |



## Hint

<details>
<summary>Hint</summary>

Keep seen values in a set. If `n` reaches 1, return True; if `n` is already in `seen`, return False (cycle).
</details>

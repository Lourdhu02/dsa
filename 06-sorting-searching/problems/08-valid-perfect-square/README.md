# 08. Valid perfect square  `[easy]`

Given a non-negative integer `num`, return True if it is a perfect square.

## Function signature

```python
def is_perfect_square(num: int) -> bool: ...
```

## Examples

| num | result |
|---|---|
| 16 | True |
| 14 | False |
| 1 | True |



## Hint

<details>
<summary>Hint</summary>

Binary-search `r` in `[1, num]`; check `r*r`.
</details>

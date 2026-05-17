# 12. Power of two  `[easy]`

Return `True` if `n` is a positive power of two (`1, 2, 4, 8, 16, ...`).

The bit trick `n > 0 and n & (n - 1) == 0` does this in `Θ(1)`. Why? A power of two has exactly one set bit; subtracting one flips that bit off and turns every lower bit on; AND-ing gives 0. Any number with more than one set bit will have at least one bit that survives the AND.

## Function signature

```python
def is_power_of_two(n: int) -> bool: ...
```

## Examples

| n | result |
|---|---|
| 1 | True |
| 16 | True |
| 1024 | True |
| 3 | False |
| 0 | False |
| -2 | False |

## Hint

<details>
<summary>Hint</summary>

`n & (n - 1) == 0` cleanly characterizes "at most one set bit". Combine with `n > 0` to reject zero / negatives.
</details>

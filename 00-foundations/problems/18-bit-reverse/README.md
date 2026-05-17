# 18. Reverse 32-bit integer  `[medium]`

Reverse the bits of a 32-bit unsigned integer.

For example, `0000 0010 1001 0100 0001 1110 1001 1100` (decimal 43261596) reversed is `0011 1001 0111 1000 0010 1001 0100 0000` (decimal 964176192).

## Function signature

```python
def reverse_bits_32(n: int) -> int: ...
```

## Examples

| n (decimal) | reversed (decimal) |
|---|---|
| 0 | 0 |
| 1 | 2147483648 |
| 43261596 | 964176192 |
| 2**32 - 1 | 2**32 - 1 |

## Constraints

- `0 <= n < 2^32`

## Hint

<details>
<summary>Hint</summary>

Pull bits off the bottom of `n` and shift them onto the top of the result. 32 iterations, constant time per iteration. There is also a divide-and-conquer bit-swap technique that does it in `Θ(log 32) = Θ(1)` operations — try that as a follow-up.
</details>

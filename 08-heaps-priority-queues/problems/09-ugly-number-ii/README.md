# 09. Ugly number II  `[medium]`

An *ugly number* has only prime factors 2, 3, 5. Return the `n`-th ugly number (1-indexed; 1 is ugly).

## Function signature

```python
def nth_ugly(n: int) -> int: ...
```

## Examples

| n | ugly[n] |
|---|---|
| 1 | 1 |
| 10 | 12 |
| 11 | 15 |



## Hint

<details>
<summary>Hint</summary>

Min-heap starting with 1. Pop smallest, push that times 2, 3, 5. Dedupe via a set.
</details>

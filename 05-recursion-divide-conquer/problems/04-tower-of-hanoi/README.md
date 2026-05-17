# 04. Tower of Hanoi  `[medium]`

Return the list of moves to transfer `n` disks from rod `"A"` to rod `"C"` using rod `"B"` as auxiliary. Each move is a tuple `(from, to)`.

## Function signature

```python
def hanoi(n: int) -> list[tuple[str, str]]: ...
```

## Examples

| n | moves |
|---|---|
| 1 | `[("A", "C")]` |
| 2 | `[("A", "B"), ("A", "C"), ("B", "C")]` |

## Constraints

- `0 <= n <= 18`


## Hint

<details>
<summary>Hint</summary>

Move n-1 from A to B (using C as aux), move the largest from A to C, move n-1 from B to C (using A as aux).
</details>

# 14. Generate parentheses  `[medium]`

Given `n` pairs of parentheses, return all well-formed strings of length `2n`.

## Function signature

```python
def generate_parenthesis(n: int) -> list[str]: ...
```

## Examples

| n | result |
|---|---|
| 3 | `["((()))","(()())","(())()","()(())","()()()"]` |
| 1 | `["()"]` |

## Constraints

- `1 <= n <= 8`


## Hint

<details>
<summary>Hint</summary>

Backtrack with two counters: opens used so far and closes used so far. Add `(` while `opens < n`; add `)` while `closes < opens`.
</details>

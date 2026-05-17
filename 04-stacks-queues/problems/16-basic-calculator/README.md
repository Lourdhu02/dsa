# 16. Basic calculator (parens, +, -)  `[hard]`

Evaluate a simple arithmetic expression containing non-negative integers, `+`, `-`, parentheses, and whitespace. No `*` or `/`.

## Function signature

```python
def calculate(s: str) -> int: ...
```

## Examples

| s | result |
|---|---|
| `"1 + 1"` | 2 |
| `" 2-1 + 2 "` | 3 |
| `"(1+(4+5+2)-3)+(6+8)"` | 23 |



## Hint

<details>
<summary>Hint</summary>

Single pass with one stack. Carry a running `result`, `sign` (+1 / -1) and a `number` accumulator. On `(`, push `result` and `sign`, reset. On `)`, finalize and multiply by the popped sign.
</details>

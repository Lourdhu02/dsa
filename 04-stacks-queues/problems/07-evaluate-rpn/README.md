# 07. Evaluate Reverse Polish Notation  `[medium]`

Evaluate an arithmetic expression in RPN (postfix). Tokens are integers or `+`, `-`, `*`, `/`. Integer division truncates toward zero.

## Function signature

```python
def eval_rpn(tokens: list[str]) -> int: ...
```

## Examples

| tokens | result |
|---|---|
| `["2","1","+","3","*"]` | 9 |
| `["4","13","5","/","+"]` | 6 |
| `["10","6","9","3","+","-11","*","/","*","17","+","5","+"]` | 22 |



## Hint

<details>
<summary>Hint</summary>

Stack: push numbers; on an operator, pop two, apply, push the result. For division, use `int(a / b)` to truncate toward zero (NOT `a // b` which floors).
</details>

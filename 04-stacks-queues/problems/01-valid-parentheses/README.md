# 01. Valid parentheses  `[easy]`

Given a string containing only `()[]{}`, return True iff every opener has a matching closer in the right order.

## Function signature

```python
def is_valid(s: str) -> bool: ...
```

## Examples

| s | result |
|---|---|
| `"()"` | True |
| `"()[]{}"` | True |
| `"(]"` | False |
| `"([)]"` | False |



## Hint

<details>
<summary>Hint</summary>

Push openers onto a stack. On a closer, pop and check it matches.
</details>

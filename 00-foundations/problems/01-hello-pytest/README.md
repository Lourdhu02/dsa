# 01. Hello, pytest  `[easy]`

Smoke test that confirms your toolchain is wired up. Return the string `"hello, pytest"` from `greet()`.

## Function signature

```python
def greet() -> str: ...
```

## Examples

| call | expected |
|---|---|
| `greet()` | `"hello, pytest"` |

## Constraints

None — this is a one-liner.

## Run

```
pytest 00-foundations/problems/01-hello-pytest/tests -q
```

## Hint

<details>
<summary>Hint</summary>

Just `return "hello, pytest"`. The point is to see green output, not to think.
</details>

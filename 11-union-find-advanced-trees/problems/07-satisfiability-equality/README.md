# 07. Satisfiability of equality equations  `[medium]`

Given equations like `a==b` and `c!=d`, return True iff they're all satisfiable.

## Function signature

```python
def equations_possible(equations: list[str]) -> bool: ...
```

## Examples

| equations | result |
|---|---|
| `["a==b","b!=a"]` | False |
| `["a==b","b==c","a==c"]` | True |
| `["a!=a"]` | False |



## Hint

<details>
<summary>Hint</summary>

Union all `==` constraints first, then verify each `!=` constraint connects different components.
</details>

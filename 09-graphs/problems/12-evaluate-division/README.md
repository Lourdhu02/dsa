# 12. Evaluate division  `[medium]`

Given `equations[i] = [A, B]` and `values[i] = A / B`, answer `queries[i] = [C, D]` returning `C / D` or `-1.0` if undetermined.

## Function signature

```python
def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]: ...
```

## Examples

```
equations=[["a","b"],["b","c"]], values=[2.0, 3.0]
queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
answer  =[6.0,    0.5,    -1.0,   1.0,    -1.0]
```



## Hint

<details>
<summary>Hint</summary>

Treat each variable as a node; an equation `a/b = v` means edge `a -> b` weight `v` and `b -> a` weight `1/v`. For each query DFS from C accumulating the product.
</details>

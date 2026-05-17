# 02. Min stack  `[easy]`

Design a stack supporting `push`, `pop`, `top`, and `get_min` — all in `Θ(1)`.

## Function signature

```python
class MinStack:
    def push(self, x: int) -> None: ...
    def pop(self) -> None: ...
    def top(self) -> int: ...
    def get_min(self) -> int: ...
```

## Examples

```
ms = MinStack()
ms.push(-2); ms.push(0); ms.push(-3)
ms.get_min()   # -3
ms.pop()
ms.top()       # 0
ms.get_min()   # -2
```



## Hint

<details>
<summary>Hint</summary>

Maintain a parallel `min_stack` whose top is the min of everything in the main stack at that depth.
</details>

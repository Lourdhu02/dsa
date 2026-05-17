# 03. Implement queue using stacks  `[easy]`

Implement a FIFO queue using only two stacks. Support `push`, `pop`, `peek`, `empty`. Amortized `Θ(1)` per op.

## Function signature

```python
class MyQueue:
    def push(self, x: int) -> None: ...
    def pop(self) -> int: ...
    def peek(self) -> int: ...
    def empty(self) -> bool: ...
```

## Examples

```
q = MyQueue()
q.push(1); q.push(2); q.peek()  # 1
q.pop()                         # 1
q.empty()                       # False
```



## Hint

<details>
<summary>Hint</summary>

Two stacks: `in_stack` for pushes, `out_stack` for pops. When `out_stack` is empty, drain `in_stack` into it (reversing order).
</details>

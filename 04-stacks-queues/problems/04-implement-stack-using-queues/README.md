# 04. Implement stack using queues  `[easy]`

Implement a LIFO stack using only a queue (`collections.deque` allowed for FIFO semantics). Support `push`, `pop`, `top`, `empty`.

## Function signature

```python
class MyStack:
    def push(self, x: int) -> None: ...
    def pop(self) -> int: ...
    def top(self) -> int: ...
    def empty(self) -> bool: ...
```

## Examples

```
s = MyStack()
s.push(1); s.push(2); s.top()  # 2
s.pop()                         # 2
s.empty()                       # False
```



## Hint

<details>
<summary>Hint</summary>

After each push, rotate the queue so the just-added element is at the front. Then `pop` and `top` are constant-time on the queue front.
</details>

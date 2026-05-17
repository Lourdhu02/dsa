# 14. Design circular queue  `[medium]`

Implement `MyCircularQueue` with fixed capacity, `Θ(1)` per op. Support `en_queue`, `de_queue`, `front`, `rear`, `is_empty`, `is_full`.

## Function signature

```python
class MyCircularQueue:
    def __init__(self, k: int) -> None: ...
    def en_queue(self, value: int) -> bool: ...
    def de_queue(self) -> bool: ...
    def front(self) -> int: ...
    def rear(self) -> int: ...
    def is_empty(self) -> bool: ...
    def is_full(self) -> bool: ...
```

## Examples

```
q = MyCircularQueue(3)
q.en_queue(1)      # True
q.en_queue(2)      # True
q.en_queue(3)      # True
q.en_queue(4)      # False (full)
q.rear()           # 3
q.is_full()        # True
q.de_queue()       # True
q.en_queue(4)      # True
q.rear()           # 4
```



## Hint

<details>
<summary>Hint</summary>

Fixed array, head and tail indices, size counter. Wrap with `% k`.
</details>

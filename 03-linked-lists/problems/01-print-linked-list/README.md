# 01. Build and print a linked list  `[easy]`

Given a Python list `xs`, build a singly-linked list with those values and return the head. Then implement `to_list(head)` that materializes a linked list as a Python list. Both must run in `Θ(n)` time.

## Function signature

```python
class ListNode:
    def __init__(self, val=0, next=None): ...

def build(xs: list[int]) -> ListNode | None: ...
def to_list(head: ListNode | None) -> list[int]: ...
```

## Examples

| xs | to_list(build(xs)) |
|---|---|
| `[]` | `[]` |
| `[1, 2, 3]` | `[1, 2, 3]` |



## Hint

<details>
<summary>Hint</summary>

Walk `xs` left to right, maintaining a tail pointer so each append is Θ(1).
</details>

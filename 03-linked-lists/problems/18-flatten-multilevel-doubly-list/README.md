# 18. Flatten a multilevel doubly linked list  `[medium]`

Each node in a doubly-linked list has `prev`, `next`, and `child` pointers. `child` may point to a separate doubly-linked list (which may itself have children). Flatten the structure depth-first into a single-level doubly-linked list.

## Function signature

```python
class Node:
    val: int
    prev: 'Node | None'
    next: 'Node | None'
    child: 'Node | None'

def flatten(head: Node | None) -> Node | None: ...
```

## Examples

```
1 <-> 2 <-> 3
      |
      4 <-> 5
```

becomes

```
1 <-> 2 <-> 4 <-> 5 <-> 3
```



## Hint

<details>
<summary>Hint</summary>

Walk left to right. When you see `cur.child`, splice the child sublist between `cur` and `cur.next`. Use a stack to remember the original `cur.next` to attach after the child sublist's tail.
</details>

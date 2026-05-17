# 05. Find cycle start  `[medium]`

If the linked list has a cycle, return the node where the cycle begins, else return `None`. Run in `Θ(n)` time, `Θ(1)` extra space.

## Function signature

```python
def detect_cycle(head: ListNode | None) -> ListNode | None: ...
```

## Examples

Same shape as problem 04 but return the cycle-entry node, not a bool.



## Hint

<details>
<summary>Hint</summary>

After Floyd detects a meeting point inside the cycle, restart one pointer at `head` and advance both by 1 step. They meet at the cycle entrance.
</details>

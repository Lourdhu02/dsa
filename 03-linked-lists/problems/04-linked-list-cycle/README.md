# 04. Linked list cycle detection  `[easy]`

Given the head of a linked list, return `True` if the list contains a cycle, else `False`. Run in `Θ(n)` time, `Θ(1)` extra space.

## Function signature

```python
def has_cycle(head: ListNode | None) -> bool: ...
```

## Examples

```
1 -> 2 -> 3 -> 4
          ^---------+
                    |
                  (4.next = 2)
```

Has a cycle starting at 2.



## Hint

<details>
<summary>Hint</summary>

Floyd's tortoise and hare. Slow moves 1 step, fast moves 2. If they meet, there's a cycle. If fast hits None, there isn't.
</details>

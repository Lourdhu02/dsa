# 08. Palindrome linked list  `[medium]`

Return `True` if the singly-linked list reads the same forward and backward. Solve in `Θ(n)` time, `Θ(1)` extra space.

## Function signature

```python
def is_palindrome(head: ListNode | None) -> bool: ...
```

## Examples

| list | result |
|---|---|
| `1->2->2->1` | True |
| `1->2` | False |
| `1` | True |



## Hint

<details>
<summary>Hint</summary>

Find the midpoint with fast/slow, reverse the second half in place, then walk the two halves in lockstep comparing values. Optionally restore the list afterwards.
</details>

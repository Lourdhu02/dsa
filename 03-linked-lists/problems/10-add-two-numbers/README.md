# 10. Add two numbers  `[medium]`

Two non-negative integers are represented as linked lists, with each node holding one digit in REVERSE order (so `342` is `2->4->3`). Return the sum as a linked list in the same order.

## Function signature

```python
def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None: ...
```

## Examples

| a | b | result |
|---|---|---|
| `2->4->3` (342) | `5->6->4` (465) | `7->0->8` (807) |
| `0` | `0` | `0` |
| `9->9` | `1` | `0->0->1` (100) |



## Hint

<details>
<summary>Hint</summary>

Walk both lists together; carry propagates digit by digit.
</details>

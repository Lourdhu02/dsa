# 03. Merge two sorted lists  `[easy]`

Merge two sorted singly-linked lists into one sorted list. Return the new head.

## Function signature

```python
def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None: ...
```

## Examples

| a | b | merged |
|---|---|---|
| `1->2->4` | `1->3->4` | `1->1->2->3->4->4` |
| `[]` | `[]` | `[]` |
| `[]` | `0` | `0` |



## Hint

<details>
<summary>Hint</summary>

Sentinel head + tail pointer; walk both lists picking the smaller; append the remainder.
</details>

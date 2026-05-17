class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def odd_even_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    odd = head
    even_head = head.next
    even = even_head
    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

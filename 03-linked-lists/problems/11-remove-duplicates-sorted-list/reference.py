class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode | None) -> ListNode | None:
    cur = head
    while cur is not None and cur.next is not None:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

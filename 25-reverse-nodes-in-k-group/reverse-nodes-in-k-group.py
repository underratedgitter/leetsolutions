class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        tail = None

        while curr:
            # Find the group of size k
            group_start = curr
            for _ in range(k - 1):
                curr = curr.next
                if not curr:
                    break

            # If the group size is less than k, do not reverse
            if not curr:
                break

            next_head = curr.next
            curr.next = None
            prev.next, tail = self.reverseLinkedList(group_start, None)
            group_start.next = next_head
            prev = group_start
            curr = next_head

        return dummy.next

    def reverseLinkedList(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        prev = None
        curr = head

        while curr != tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        if tail:
            tail.next = prev

        return prev, head
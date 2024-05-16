# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # Create a dummy node to simplify the logic
        curr = dummy  # Initialize the current node to the dummy node
        carry = 0  # Initialize the carry to 0

        # Traverse both linked lists until both are None
        while l1 or l2:
            # Get the values of the current digits from both lists
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = carry + x + y
            carry = total // 10
            curr.next = ListNode(total % 10)  # Create a new node with the digit value
            curr = curr.next  # Move to the next node

            # Move to the next digits in both lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there is a remaining carry, create a new node for it
        if carry:
            curr.next = ListNode(carry)

        return dummy.next  # Return the head of the new linked list (excluding the dummy node)
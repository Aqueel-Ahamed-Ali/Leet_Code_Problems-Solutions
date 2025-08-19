# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy node and current pointer
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists or until carry remains
        while l1 or l2 or carry:
            # Get values (use 0 if list is exhausted)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Compute sum and new carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node for the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result list (skip dummy node)
        return dummy.next

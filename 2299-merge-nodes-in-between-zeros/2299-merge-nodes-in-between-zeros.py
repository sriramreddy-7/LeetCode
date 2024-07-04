# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        head = head.next
        while head:
            current_sum = 0
            while head and head.val != 0:
                current_sum += head.val
                head = head.next
            if head:
                head = head.next
            current.next = ListNode(current_sum)
            current = current.next
        
        return dummy.next
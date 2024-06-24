# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        prev=None
        while t!=None:
            nxt=t.next
            t.next=prev
            prev=t
            t=nxt
        head=prev
        return head

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        t=head
        p=None
        while t!=None and t.val==val:
            head=t.next
            t=head
        while t!=None:
            if t.val==val:
                p.next=t.next
                t=p.next
            else:
                p=t
                t=t.next
        return head            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None 
        if head.next.next==None:
            head.next=None
            return head
        p=head.next.next
        q=head
        while p and p.next:
            p = p.next.next
            q = q.next
        q.next=q.next.next
        return head

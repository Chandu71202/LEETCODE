# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        q=head
        c=0
        while(p!=None):
            p=p.next
            c+=1
        if(c==n):
            head=head.next
            return head
        for i in range(0,c-n-1):
            q=q.next
        q.next=q.next.next
        return head

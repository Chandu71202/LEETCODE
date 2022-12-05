# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        q = head
        while(p and p.next):
            p = p.next.next
            q = q.next
        
        pre = None
        fwd = q
        while(fwd):
            fwd = q.next
            q.next=pre
            pre=q
            q=fwd
        
        ans = float('-inf')
        while(pre):
            ans = max(ans,head.val+pre.val)
            head = head.next
            pre = pre.next
        return ans
                

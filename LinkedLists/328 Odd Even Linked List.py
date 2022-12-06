# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newOddHead = ListNode(0)
        newEvenHead = ListNode(0)
        temp1 = newOddHead
        temp2 = newEvenHead
        isOdd = True
        while(head):
            if isOdd:
                newOddHead.next = head
                newOddHead = newOddHead.next
            else:
                newEvenHead.next = head
                newEvenHead = newEvenHead.next
            head = head.next
            isOdd = not isOdd
        newEvenHead.next = None
        newOddHead.next = temp2.next
        return temp1.next

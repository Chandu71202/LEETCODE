/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        int count=0;
        ListNode* p=head;
        ListNode* q=head;
        while(p!=NULL)
        {
            p=p->next;
            count+=1;
        }
        if(count==n)
        {
            head=head->next;
            return head;
        }
        for(int i=0;i<count-n-1;i++)
        {
            q=q->next;
        }
        q->next=q->next->next;
        return head;
    }
};

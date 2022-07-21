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
    ListNode* deleteMiddle(ListNode* head) 
    {
        ListNode* p=head;
        ListNode* q=NULL;
        if(p->next==NULL)
        {
            return q;
        }
        if(p->next->next==NULL)
        {
            p->next=NULL;
            return p;
        }
        int count=0;
        q=head;
        ListNode* r=head;
        while(p!=NULL && p->next!=NULL)
        {
            count+=1;
            p=p->next->next;
            q=q->next;
        }
        for(int i=0;i<count-1;i++)
        {
            r=r->next;
        }
        r->next=q->next;
        return head;
        
        
//         p=head->next->next;
//         q=head;
//         while(p!=NULL && p->next!=NULL)
//         {
//             p=p->next->next;
//             q=q->next;
//         }
//         q->next=q->next->next;
//         return head;
    }
};

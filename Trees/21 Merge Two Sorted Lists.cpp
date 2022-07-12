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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) 
    {
        struct ListNode* p=list1;
        struct ListNode* q=list2;
        struct ListNode *s,*newhead;
        if(p==NULL) return q;
        if(q==NULL) return p;
        if(p&&q)
        {
            if(p->val<q->val)
            {
                s=p;
                p=p->next;
            }
            else{
                s=q;
                q=q->next;
            }
            newhead=s;
        }
        while(p&&q)
        {
            if(p->val<q->val)
            {
                s->next=p;
                s=p;
                p=p->next;
            }
            else
            {
                s->next=q;
                s=q;
                q=q->next;
            }
        }
            if(p==NULL)
            {
                s->next=q;
            }
            else
            {
                s->next=p;
            }
        return newhead;
    }
};

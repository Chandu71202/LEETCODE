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
    ListNode* find(ListNode* head,int k)
    {
        ListNode* p=head;
        ListNode* q=head;
        int count=1;
        while(p->next!=NULL)
        {
            p=p->next;
            count+=1;
        }
        for(int i=0;i<count-k;i++)
        {
            q=q->next;
        }
        return q;
    }
    ListNode* swapNodes(ListNode* head, int k) 
    {
        ListNode* p=head;
        ListNode* q=head;
        for(int i=0;i<k-1;i++)
        {
            p=p->next;
        }
        q=find(head,k);
        int temp;
        temp=p->val;
        p->val=q->val;
        q->val=temp;
        return head;
    }
    // ListNode* swapNodes(ListNode* head, int k)
    // {
    //     ListNode* p=head;
    //     ListNode* q=head;
    //     ListNode* temp=head;
    //     int count=1;
    //     while(temp!=NULL)
    //     {
    //         if(count<k)
    //             p=p->next;
    //         if(count>k)
    //             q=q->next;
    //         temp=temp->next;
    //         count+=1;
    //     }
    //     int temp1;
    //     temp1=p->val;
    //     p->val=q->val;
    //     q->val=temp1;
    //     return head;
    // }
};

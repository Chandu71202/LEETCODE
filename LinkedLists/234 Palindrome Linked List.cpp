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
    struct ListNode* reverse(struct ListNode* head)
    {
        struct ListNode* curr=head;
        struct ListNode* prev=NULL;
        struct ListNode* fwd;
        while(curr!=NULL)
        {
            fwd=curr->next;
            curr->next=prev;
            prev=curr;
            curr=fwd;
        }
        head=prev;
        return head;

    }

    bool Compare2LL(struct ListNode* head1,struct ListNode* head2)
    {
        struct ListNode* p1=head1;
        struct ListNode* p2=head2;

        while(p1&&p2)
        {
            if(p1->val==p2->val)
            {
                p1=p1->next;
                p2=p2->next;
            }
            else
            {
                return false;
            }
        }
        return true;

    }

    bool isPalindrome(ListNode* head) 
    {
        struct ListNode* newhead=(struct ListNode*)malloc(sizeof(struct ListNode));
        struct ListNode* p=head;
        struct ListNode* q=head;
        if(p->next==NULL)
        {
            return true;
        }
        while(1)
        {
            p=p->next->next;
            if(p==NULL)
            {
                newhead=q->next;
                q->next=NULL;
                break;
            }
            if(p->next==NULL)
            {
                newhead=q->next->next;
                q->next=NULL;
                break;
            }
            q=q->next;
        }
        newhead=reverse(newhead);
        return Compare2LL(head,newhead);
    }
};

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
    ListNode* oddEvenList(ListNode* head) 
    {
        ListNode* EvenHead = new ListNode(0);
        ListNode* OddHead = new ListNode(0);
        ListNode* evenNode = EvenHead;
        ListNode* oddNode = OddHead;
        bool isEven = true;
        while(head)
        {
            if(isEven)
            {
                isEven = false;
                EvenHead->next = head;
                EvenHead = EvenHead->next;
            }
            else
            {
                isEven = true;
                OddHead->next = head;
                OddHead = OddHead->next;
            }
            head = head->next;
        }
        OddHead->next = NULL;
        EvenHead->next = oddNode->next;
        return evenNode->next;
    }
};

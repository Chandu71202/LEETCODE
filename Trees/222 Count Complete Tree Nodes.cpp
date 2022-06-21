/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <math.h>
class Solution {
public:
    int countNodes(TreeNode* root) 
    {
        if(root==NULL)
            return 0;
        int leftlevels=1,rightlevels=1;
        TreeNode* l =root->left;
        while(l)
        {
            l=l->left;
            leftlevels+=1;
        }
        TreeNode* r =root->right;
        while(r)
        {
            r=r->right;
            rightlevels+=1;
        }
        if(leftlevels==rightlevels)
            return pow(2,leftlevels)-1;
        else
            return 1+countNodes(root->left)+countNodes(root->right);
    }
};

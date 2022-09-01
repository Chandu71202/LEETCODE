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
class Solution {
public:
    int c=0;
    int goodNodes(TreeNode* root) 
    {
        if(root==NULL)
            return c;
        helper(root,root->val);
        return c;
    }
    void helper(TreeNode* root,int val)
    {
        if(root==NULL)
            return;
        if(root->val>=val)
            c++;
        helper(root->left,max(root->val,val));
        helper(root->right,max(root->val,val));
    }
    
};

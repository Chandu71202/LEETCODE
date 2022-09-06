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
    TreeNode* pruneTree(TreeNode* root) 
    {
        if(root==NULL)
            return NULL;
        root->left=pruneTree(root->left);
        root->right=pruneTree(root->right);
        if(root->left!=NULL || root->right!=NULL)
            return root;
        else
        {
            if(root->val==1)
                return root;
            else
                return NULL;
        }
    }
};

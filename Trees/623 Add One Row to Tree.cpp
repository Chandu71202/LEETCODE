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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) 
    {
        if(depth==1)
        {
            TreeNode* temp = new TreeNode(val);
            temp->left=root;
            return temp;
        }
        helper(root,val,depth,1);
        return root;
    }
    
    void helper(TreeNode* root, int val,int depth, int maxdepth)
    {
        if(root==NULL)
            return;
            
        if(depth-1 == maxdepth)
        {
            TreeNode* temp = root->left;
            root->left = new TreeNode(val);
            root->left->left = temp;
            temp = root->right;
            root->right = new TreeNode(val);
            root->right->right = temp;
        }
        else
        {
            helper(root->left,val,depth,maxdepth+1);
            helper(root->right,val,depth,maxdepth+1);
        }
    }
};

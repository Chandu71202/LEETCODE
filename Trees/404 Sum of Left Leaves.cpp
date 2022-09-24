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
    int sum=0;
    int sumOfLeftLeaves(TreeNode* root) {
        traversal(root);
        return sum;
    }
    int traversal(TreeNode *t)
    {
        if(t==NULL)
            return 0;
        if(!(t->left||t->right))
        {
            return  t->val;
        }
        sum+=traversal(t->left);
        traversal(t->right);  
        return 0;
    }
};

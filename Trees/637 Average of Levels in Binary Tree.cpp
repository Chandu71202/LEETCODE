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
class Solution 
{
public:
    vector<double> averageOfLevels(TreeNode* root) 
    {
        vector<double> result;
        if(root==NULL)
            return result;
        queue<TreeNode*> nodesQueue;
        nodesQueue.push(root);
        while(!nodesQueue.empty())
        {
            int size=nodesQueue.size();
            long temp=0;
            for(int i=0;i<size;i++)
            {
                TreeNode* node=nodesQueue.front();
                nodesQueue.pop();
                if(node->left)
                    nodesQueue.push(node->left);
                if(node->right)
                    nodesQueue.push(node->right);
                temp+=node->val;
            }
            result.push_back((double)temp/size);
        }
        return result;
    }
};

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
#include <queue>
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) 
    {
        vector<vector<int>>res;
        if(root==NULL)
            return res;
        queue<TreeNode*> nodesQueue;
        nodesQueue.push(root);
        bool leftToright=true;
        while(!nodesQueue.empty())
        {
            int size=nodesQueue.size();
            vector<int> row(size);
            for(int i=0;i<size;i++)
            {
                TreeNode* node=nodesQueue.front();
                nodesQueue.pop();
                int index=(leftToright) ? i : size-i-1;
                row[index]=node->val;
                if(node->left)
                    nodesQueue.push(node->left);
                if(node->right)
                    nodesQueue.push(node->right);
            }
        leftToright=!leftToright;
        res.push_back(row);
        }
    return res;
    }
};

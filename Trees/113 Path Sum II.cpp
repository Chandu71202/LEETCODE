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
    void findPaths(TreeNode* node, int sum, vector<int>& path, vector<vector<int>>& ans) 
    {
        if (node==NULL) 
            return;
        path.push_back(node -> val);
        if ((node -> left==NULL && node -> right == NULL) && sum == node -> val)
            ans.push_back(path);
        findPaths(node -> left, sum - node -> val, path, ans);
        findPaths(node -> right, sum - node -> val, path, ans);
        path.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) 
    {
        vector<int> path;
        vector<vector<int>> ans;
        findPaths(root, targetSum, path, ans);
        return ans;
    }
};

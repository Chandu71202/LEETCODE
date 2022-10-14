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
    vector<vector<int>> res;
    void preorder(TreeNode* root,vector<int> ans)
    {
        if(root)
        {
            if (root->left==NULL && root->right==NULL)
            {
                ans.push_back(root->val);
                res.push_back(ans);
            }
            else
            {
                ans.push_back(root->val);
                preorder(root->left,ans);
                preorder(root->right,ans);
            }
        }
    }
    vector<string> binaryTreePaths(TreeNode* root) 
    {
        vector<int> ans;
        preorder(root,ans);
        vector<string> ans1;

        for (int i = 0; i < res.size(); i++)
        {
            string s="";
            int j;
            for (j = 0; j < res[i].size()-1; j++)
            {
                s+=to_string(res[i][j])+"->";
            }
            s+=to_string(res[i][j++]);
            ans1.push_back(s);
        }
        return ans1;
    }
};

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def preorder(root,l):
            if root: 
                if (root.left==None and root.right==None):
                    res.append(l+[root.val])
                else:
                    preorder(root.left,l+[root.val])
                    preorder(root.right,l+[root.val])
                
        preorder(root,[])
        return [('->'.join([str(k) for k in i]))for i in res]
            

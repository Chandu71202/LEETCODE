# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root1,root2):
        if (root1==None and root2==None):
            return True
        elif (root1 == None or root2 == None or root1.val!=root2.val):
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left,root.right)

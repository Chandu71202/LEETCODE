# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse1(self,root):
        if not root:
            return 
        if(root.left==None and root.right==None):
            self.s1+=str(root.val)+" "
        self.traverse1(root.left)
        self.traverse1(root.right)

    def traverse2(self,root):
        if not root:
            return 
        if(root.left==None and root.right==None):
            self.s2+=str(root.val)+" "
        self.traverse2(root.left)
        self.traverse2(root.right)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.s1=""
        self.s2=""
        self.traverse1(root1)
        self.traverse2(root2)
        return self.s1==self.s2

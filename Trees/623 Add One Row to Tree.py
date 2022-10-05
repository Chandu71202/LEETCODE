# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            temp = TreeNode(val)
            temp.left=root
            return temp
        self.AddingTheRow(root,val,depth,1)
        return root
        
    
    def AddingTheRow(self,root,val,depth,level):
        
        if root==None:
            return
        
        if depth-1==level:
            
            temp = root.left
            root.left = TreeNode(val)
            root.left.left = temp
            temp = root.right
            root.right = TreeNode(val)
            root.right.right = temp
            
        else:
            
            self.AddingTheRow(root.left,val,depth,level+1)
            self.AddingTheRow(root.right,val,depth,level+1)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        stack = []
        stack.append(root)
        res = ""
        while stack:
            node = stack.pop()
            if node == ")":
                res += ")"
                continue
            res += "("+str(node.val)
            if not node.left and  node.right:
                res += "()"
            if  node.right:
                stack.append(")")
                stack.append(node.right)
            if  node.left:
                stack.append(")")
                stack.append(node.left)

        return res[1:]

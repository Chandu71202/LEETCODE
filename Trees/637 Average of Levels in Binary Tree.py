# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for l in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return_list.append(sum(ans)/len(ans))
        return return_list
        

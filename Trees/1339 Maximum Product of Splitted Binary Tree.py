class Solution:
    def sumedTree(self, node):
        if node == None:
            return 0
        
        left_sum = self.sumedTree(node.left)
        
        right_sum = self.sumedTree(node.right)
        
        node.val += left_sum + right_sum
        
        return node.val
        
    def cutEdge(self, node, total, res):
        if node == None:
            return
        
        self.cutEdge(node.left, total, res)
        
        self.cutEdge(node.right, total, res)
        
        res[0] = max(res[0], node.val * (total - node.val))
		
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sumedTree(root)
        
        res = [0]
        
        total = root.val
        
        self.cutEdge(root, total, res)
        
        return res[0] % (10 ** 9 + 7)

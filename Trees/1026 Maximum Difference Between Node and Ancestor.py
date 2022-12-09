# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self._max_ancestor_diff(root, root.val, root.val)

    def _max_ancestor_diff(self, root: TreeNode, max_ancestor_val: int, min_ancestor_val: int) -> int:
        if root is None:
            return 0
        return max(
            abs(max_ancestor_val - root.val),
            abs(min_ancestor_val - root.val),
            self._max_ancestor_diff(
                root.left, max(max_ancestor_val, root.val), min(min_ancestor_val, root.val)),
            self._max_ancestor_diff(
                root.right, max(max_ancestor_val, root.val), min(min_ancestor_val, root.val))
        )

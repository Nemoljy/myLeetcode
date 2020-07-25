# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l_dep = self.maxDepth(root.left)
        r_dep = self.maxDepth(root.right)
        return max(l_dep,r_dep)+1
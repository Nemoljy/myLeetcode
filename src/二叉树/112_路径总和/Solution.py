# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## 2 递归 sum-val
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root:
            return False
        if not node.left and not node.right:
            return sum==root.val
        return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)

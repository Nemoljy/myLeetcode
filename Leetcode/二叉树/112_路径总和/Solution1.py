# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        
## 1 计算所有路径的和
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def traverse_sum(node,s):
            if node:
                s += node.val
                if not node.left and not node.right:
                    sums.append(s)
                traverse_sum(node.left,s)
                traverse_sum(node.right,s)
        sums = []
        traverse_sum(root,0)
        return True if sum in sums else False

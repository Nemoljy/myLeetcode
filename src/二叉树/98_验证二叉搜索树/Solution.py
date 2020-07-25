# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre = -9999999999999999999999
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False

        if root.val <= self.pre:
            return False
        
        self.pre = root.val

        return self.isValidBST(root.right)
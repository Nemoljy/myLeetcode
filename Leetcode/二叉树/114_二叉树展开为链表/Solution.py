# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        helper = []  ## 需要额外存储空间
        def traverse(node):
            if not node: return
            helper.append(node)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        node = root
        for i in range(1,len(helper)):
            node.right = helper[i]
            node.left = None
            node = node.right
        return
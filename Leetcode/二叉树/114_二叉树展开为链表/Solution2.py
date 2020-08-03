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
        ## 寻找前驱节点
        curr = root
        while curr:
            if curr.left:
                pre = nxt = curr.left
                while pre.right:
                    pre = pre.right  ## 左子树的最右节点为前驱节点
                pre.right = curr.right  ## 右子树接到前驱节点下
                curr.left = None
                curr.right = nxt
            curr = curr.right
        return
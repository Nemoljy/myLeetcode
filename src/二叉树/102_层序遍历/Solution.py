# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result, level_temp = [], []
        nodes = [root, "level"]
        while nodes:
            temp = nodes.pop(0)
            if temp == "level":
                result.append(level_temp)
                level_temp = []
                if nodes:
                    nodes.append("level")
                    continue
                else:
                    break
            if temp.element is not None:
                level_temp.append(temp.element)
            if temp.left is not None:
                nodes.append(temp.left)
            if temp.right is not None:
                nodes.append(temp.right)
        return result

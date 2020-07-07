# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        ## 遍历所有路径
        def traverse_sum(node,path):
            if node:
                path += str(node.val)

                if not node.left and not node.right:
                    paths.append(path)
                path += '->' 
                traverse_sum(node.left,path)
                traverse_sum(node.right,path)
                
        paths = []
        traverse_sum(root,'')
        return paths

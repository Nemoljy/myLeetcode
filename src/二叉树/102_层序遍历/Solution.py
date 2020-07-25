# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        res = []
        tmp_layer = []
        queue.append([root,0]) # [node，行数]
        while len(queue):
            tmp_node = queue.pop(0)
            tmp_layer.append(tmp_node[0].val)
            if len(queue):
                if tmp_node[1] != queue[0][1]:
                    res.append(tmp_layer[:])
                    tmp_layer = []
            else:
                res.append(tmp_layer[:])
                tmp_layer = []
            if tmp_node[0].left:
                queue.append([tmp_node[0].left,tmp_node[1]+1])
            if tmp_node[0].right:
                queue.append([tmp_node[0].right,tmp_node[1]+1])
        return res
                
            
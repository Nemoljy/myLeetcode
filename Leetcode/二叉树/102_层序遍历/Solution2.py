## 不用额外空间，而是每次循环都pop出所有


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
        queue.append(root)
        while len(queue):
            tmp_q = queue[:]
            queue = []
            tmp_layer = [k.val for k in tmp_q]
            res.append(tmp_layer[:])
            for tmp_node in tmp_q:
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
            
        return res
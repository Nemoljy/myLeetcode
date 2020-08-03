# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 自己写的
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return []
        node = head
        dic = {}
        while node:
            dic[node] = 1  # 1的保留  0的去掉  默认为1
            node = node.next
        node = head
        while node.next:
            if node.val == node.next.val:
                dic[node] = 0
                dic[node.next] = 0
            node = node.next
        res = [k for k,v in dic.items() if v==1]

        rhead = None
        if len(res):
            rhead = res[0]
            rhead.next = None
            for i in range(len(res)-1):
                res[i].next = res[i+1]
            res[-1].next = None

        return rhead
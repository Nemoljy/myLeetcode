## 改进版，用哑节点dummy，避免判断边界情况：n=1，n=l，n=l=1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        lenth = 0
        node = head
        while node:
            node = node.next
            lenth += 1
        node = dummy
        for i in range(lenth-n):
            node = node.next
        node.next = node.next.next
        
        return dummy.next

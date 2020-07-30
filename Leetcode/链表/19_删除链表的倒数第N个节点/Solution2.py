## 遍历一次 双指针  指针间隔n
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy
        i = 0
        while right.next:
            right = right.next
            i += 1
            if i > n:
                left = left.next
        
        left.next = left.next.next
        return dummy.next

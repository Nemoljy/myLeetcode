# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 其实也是自己写的  双指针
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return []
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        while head and head.next:
            if head.val == head.next.val:  ## 出现重复情况，这次的重复扫完后删掉
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:  ## 没重复，正常遍历下去
                prev = head
            head = head.next
        return dummy.next
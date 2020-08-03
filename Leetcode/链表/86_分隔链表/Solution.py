# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        right,left = ListNode(None),ListNode(None)
        rcurr,lcurr = right,left
        while head:
            if head.val<x:
                lcurr.next = head
                lcurr = lcurr.next
            else:
                rcurr.next = head
                rcurr = rcurr.next
            head = head.next
        rcurr.next = None  ## 关键，不然右半段连着过去了
        lcurr.next = right.next
        return left.next
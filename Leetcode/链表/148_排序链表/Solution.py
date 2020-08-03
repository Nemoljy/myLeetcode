# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:  ## 递归 O(n) 和 O(logn) 空间复杂度不符合题意
        if not head or not head.next: return head
        slow,fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None ## cut

        ## 递归
        left, right = self.sortList(head), self.sortList(mid)

        ## 合并
        curr = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                curr.next, left = left, left.next
            else:
                curr.next, right = right, right.next
            curr = curr.next
        curr.next = left if left else right
        return res.next
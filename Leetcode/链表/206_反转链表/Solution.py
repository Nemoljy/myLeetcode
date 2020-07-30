class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = head
        prev = ListNode(None)
        prev.next = curr

        ## 输入[1,2,3,4,5]   2   4为例
        for i in range(m):
            if i == m-1:
                left = prev  ## left为1
            prev = prev.next
            curr = curr.next  
        ## 循环完之后  prev为1，curr为2

        ## 要换的部分倒转
        for i in range(n-m):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        ## 循环完之后：1->2->3->2->3->.....
        ## 4->3->2->3->.....  prev = 4   curr = 5

        tmp2 = left.next  ## 存2
        left.next = prev  ## 使 1->4
        tmp2.next = curr  ## 使 2->5
        
        
        return head if m != 1 else prev

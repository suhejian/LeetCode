# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = [], []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        
        while l2:
            b.append(l2.val)
            l2 = l2.next
        
        num_a, num_b = 0, 0
        for i in range(len(a)):
            num_a += a[i] * (10 ** i)
        for i in range(len(b)):
            num_b += b[i] * (10 ** i)
        res_num = num_a + num_b
        if res_num == 0:
            return ListNode(0)
        res = []
        while res_num:
            res.append(res_num % 10)
            res_num = res_num // 10
        ans = ListNode(0)
        p = ans
        for num in res:
            p.next = ListNode(num)
            p = p.next
        return ans.next
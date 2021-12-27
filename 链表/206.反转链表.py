# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        values = []
        p = head
        while p:
            values.append(p.val)
            p = p.next
        values = values[::-1]
        res = ListNode(0)
        r = res
        for i in range(len(values)):
            r.next = ListNode(val=values[i])
            r = r.next
        return res.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        num = length // 2 + 1
        q = head
        while num > 1:
            q = q.next
            num -= 1
        return q
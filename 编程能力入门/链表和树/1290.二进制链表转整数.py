# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num_list = []
        p = head
        while p:
            num_list.append(p.val)
            p = p.next
        num = "".join(str(num) for num in num_list)
        return int(num, 2)
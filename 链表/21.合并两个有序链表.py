# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        p = res
        p1, p2 = list1, list2
        # 双指针
        while p1 or p2:
            if p1 == None:
                p.next = p2
                p2 = p2.next
                p = p.next
                continue
            if p2 == None:
                p.next = p1
                p1 = p1.next
                p = p.next
                continue
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        return res.next

            
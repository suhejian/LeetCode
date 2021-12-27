# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(val=-200)
        res.next = head
        p = res
        while p and p.next:
            if p.next.val == p.val:
                # 需要删除
                p.next = p.next.next
            else:
                # 不需要删除
                p = p.next
        return res.next

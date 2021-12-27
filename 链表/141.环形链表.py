# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        res = ListNode(0)
        res.next = head
        # 快慢指针，如果有环，则快指针一定会“套圈”慢指针
        fast, slow = res, res
        while fast.next != None and slow.next != None:
            if fast.next.next != None:
                fast = fast.next.next
            else:
                # 如果没有下一个节点，则说明没有环
                return False
            slow = slow.next
            # 快指针“套圈”慢指针
            if fast == slow:
                return True
        return False
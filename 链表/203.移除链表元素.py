# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        p = res
        while p and p.next:
            # 链表删除节点一般是找到要删除节点的前一个节点
            if p.next.val == val:
                q = p.next.next
                p.next = q
            else:
                # 如果不需要删除节点，则继续向下遍历
                p = p.next
        
        return res.next
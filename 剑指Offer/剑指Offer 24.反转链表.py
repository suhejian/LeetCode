# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        这么看比较好
        输入：1->2->3->4->5->NULL
        输出：NULL<- 1 <- 2<- 3<- 4<- 5
        """
        cur, pre = head, None
        while cur:
            # 先将后一个节点保存下来，否则会丢失
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
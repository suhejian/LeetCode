# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 在链表中，删除节点时，一般找到这个节点的前一个节点
        # 此题找不到前一个节点，因此改变当前节点的值，把下一个节点当作要删除的对象
        node.val = node.next.val
        node.next = node.next.next
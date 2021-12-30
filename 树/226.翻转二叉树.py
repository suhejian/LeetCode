# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if not root:
        #     return
        # # 交换当前节点的左右节点
        # root.left, root.right = root.right, root.left
        # # 递归地交换节点的左右节点
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # # 函数返回时，说明所有的节点已经交换完成
        # return root

        # BFS
        if not root:
            return 
        queue = [root]
        while len(queue) > 0:
            # 当前节点
            node = queue.pop(0)
            # 交换当前节点的左右节点
            node.left, node.right = node.right, node.left
            # 如果当前节点的左子树不为空，则加入队列留待以后使用
            if node.left:
                queue.append(node.left)
            # 如果当前节点的右子树不为空，则加入队列留待以后使用
            if node.right:
                queue.append(node.right)
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # if not root:
        #     return
        
        # queue = [root]
        # while queue:
        #     node = queue.pop(0) # 列表左侧当成队列头, 右侧当成队列尾
        #     if node.val == val:
        #         return node
        #     if node.left:
        #         # 如果该结点存在左结点
        #         queue.append(node.left)
        #     if node.right:
        #         # 如果该结点存在右结点
        #         queue.append(node.right)
        
        # return

        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            # val只可能在root的右子树
            return self.searchBST(root.right, val)
        elif root.val > val:
            # val只可能在root的左子树
            return self.searchBST(root.left, val)
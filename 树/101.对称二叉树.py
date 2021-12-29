# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(left, right):
            if not (left or right): # 左子树和右子树都为空
                return True
            if not (left and right):    # 左子树和右子树有一个为空
                return False
            if left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)

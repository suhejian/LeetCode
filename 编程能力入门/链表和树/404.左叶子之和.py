# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        isLeaf = lambda node: not node.left and not node.right
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                if isLeaf(node.left):
                    ans += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans


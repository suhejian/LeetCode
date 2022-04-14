# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs(node, res):
        #     if not node:
        #         return
        #     dfs(node.left, res)
        #     dfs(node.right, res)
        #     res.append(node.val)
        
        # res = []
        # dfs(root, res)
        # return res

        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
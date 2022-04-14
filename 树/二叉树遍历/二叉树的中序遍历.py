# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs(node, res):
        #     if not node:
        #         return
        #     dfs(node.left, res)
        #     res.append(node.val)
        #     dfs(node.right, res)
        # res = []
        # dfs(root, res)
        # return res

        if not root:
            return []
        stack, res = [], []
        while stack or root:
            while root:
                # 一直向左遍历
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        
        return res
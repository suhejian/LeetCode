# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归解法
        # def dfs(head):
        #     if not head:
        #         return

        #     res.append(head.val)
        #     dfs(head.left)
        #     dfs(head.right)
                
        # res = []
        # dfs(root)
        # return res

        # 迭代解法
        if not root:
            return []
        stack, res = [root], []
        while len(stack) > 0:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res

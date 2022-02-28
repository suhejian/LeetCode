"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 递归
        # res = []
        # def dfs(root):
        #     if not root:
        #         return None
        #     res.append(root.val)
        #     for child in root.children:
        #         dfs(child)
        #     # return res
        # dfs(root)
        # return res

        # 迭代
        if not root:
            return None
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans
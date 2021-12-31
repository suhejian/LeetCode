# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 二叉搜索树的特点: node.left.val < node.val < node.right.val
        # 如果p和q的值都小于或大于当前节点，说明两个节点在同一侧
        res = root
        while (p.val - res.val) * (q.val - res.val) > 0:
            if p.val - res.val < 0:
                res = res.left
            else:
                res = res.right
        return res
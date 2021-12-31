# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            nums.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for i in range(len(nums)):
            temp = nums[i+1: ]
            if k - nums[i] in temp:
                return True
        return False
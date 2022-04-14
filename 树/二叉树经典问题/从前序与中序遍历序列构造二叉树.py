# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hashmap = {value: index for index, value in enumerate(inorder)}
        def build(preorder, inorder, head1, tail1, head2, tail2):
            if head1 > tail1 or head2 > tail2:
                return
            # 根节点
            num = preorder[head1]
            # 以此划分左右子树
            index_in_inorder = hashmap[num]
            root = TreeNode(num)
            root.left = build(preorder, inorder, head1 + 1, head1 + 1 + index_in_inorder - 1 - head2, head2, index_in_inorder - 1)
            root.right = build(preorder, inorder, tail1 - (tail2 - index_in_inorder - 1), tail1, index_in_inorder + 1, tail2)
            return root
        
        root = build(preorder, inorder, 0, len(inorder) - 1, 0, len(inorder) -1)
        return root
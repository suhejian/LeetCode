# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hashmap = {value: index for index, value in enumerate(inorder)}
        def build(inorder, postorder, head1, tail1, head2, tail2):
            if head1 > tail1 or head2 > tail2:
                return
            # 后续遍历的最后一个节点是根节点
            root = TreeNode(postorder[tail2])
            # 以此索引划分左右子树
            index_in_inorder = hashmap[postorder[tail2]]
            root.left = build(inorder, postorder, head1, index_in_inorder - 1, head2, head2 + index_in_inorder - 1 - head1)
            root.right = build(inorder, postorder, index_in_inorder + 1, tail1, tail2 - 1 -(tail1 - index_in_inorder - 1), tail2 - 1)
            return root
        
        root = build(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
        return root
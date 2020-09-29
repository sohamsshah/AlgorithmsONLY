# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def rec(preorder, inorder):
            if not preorder or not inorder:
                return
            root = TreeNode(preorder.pop(0))
            mid = inorder.index(root.val)
            root.left = rec(preorder, inorder[:mid])
            root.right = rec(preorder, inorder[mid+1:])
            return root
        return rec(preorder, inorder)
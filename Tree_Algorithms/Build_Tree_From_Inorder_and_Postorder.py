# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def rec(inorder, postorder):
            if not inorder or not postorder:
                return
            root = TreeNode(postorder.pop())
            mid = inorder.index(root.val)
            root.right = rec(inorder[mid+1:], postorder)
            root.left = rec(inorder[:mid], postorder)
            return root
            
        return rec(inorder, postorder)
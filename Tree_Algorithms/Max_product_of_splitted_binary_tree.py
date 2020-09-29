# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total_val = ans = 0
    def maxProduct(self, root: TreeNode) -> int:
        self.total_val = (self.total(root))
        self.helper(root)
        return self.ans%(10**9 + 7)
    def total(self,root):
        if root is None:
            return 0 
        left = self.total(root.left)
        right = self.total(root.right)
        return left + right + root.val
    def helper(self,root):
        if root is None:
            return 0 
        left = self.helper(root.left)
        right = self.helper(root.right)
        up = self.total_val - (left + right + root.val)
        self.ans = max(self.ans, left*(up + right + root.val), right*(up + left + root.val),            right* (up + left + root.val))
        return left + right + root.val 
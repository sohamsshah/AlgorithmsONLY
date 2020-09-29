# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    arr = []
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.arr = []
        self.helper(root1)
        root_1_leaves = self.arr.copy()
        self.arr = []
        self.helper(root2)
        root_2_leaves = self.arr.copy()
        return root_1_leaves == root_2_leaves
        
        
        
    def helper(self, root):
        if not root:
            return 
        if not root.left and not root.right:
            self.arr.append(root.val) 
        self.helper(root.left)
        self.helper(root.right)
        
        
        
        
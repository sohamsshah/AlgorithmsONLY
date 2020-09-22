# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:39:37 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        
        tree = []
        tree+=self.postorderTraversal(root.left)
        tree+=self.postorderTraversal(root.right)
        return tree+[root.val]
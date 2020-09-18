# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:14:00 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        left = self.rangeSumBST(root.left,L,R)
        right = self.rangeSumBST(root.right,L,R)
        if root.val in range(L,R+1):
            return root.val + left + right
        else:
            return left+right
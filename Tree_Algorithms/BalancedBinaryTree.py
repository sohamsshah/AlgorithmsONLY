# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:55:48 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if node == None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if left == 999999 or right == 999999:
                return 999999
            if abs(left-right) in range(0,2):
                return max(left,right)+1
            else:
                return 999999
        if (helper(root)) == 999999:
            return False
        else:
            return True
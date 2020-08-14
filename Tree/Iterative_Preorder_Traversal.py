# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:29:34 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return [] 
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
            ans.append(node.val)
            
        return ans 
        
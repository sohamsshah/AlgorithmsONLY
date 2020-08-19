# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:51:07 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int: 
        stack = []
        temp = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                if len(stack) == 0:
                    break
                root = stack.pop()
                temp.append(root.val)
                root = root.right
        return (temp[k-1])
    
# Alternative

def kthSmallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
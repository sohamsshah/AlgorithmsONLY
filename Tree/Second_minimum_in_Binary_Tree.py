# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:27:52 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        minimum = [9999999999,9999999999]
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            for i in range(len(minimum)):
                if root.val < minimum[i]:
                    if root.val not in minimum:
                        minimum.insert(i,root.val)
                        break
            minimum= minimum[:2]
            root= root.right
        if minimum[-1] == 9999999999:
            return -1
        return minimum[-1]
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:14:35 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    self.count = 0
    def pathSum(self, root, sum): 
        rst = []
        self.dfs(root, sum,rst, [])
        return rst
    def dfs(self, root, sum, rst, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if not sum - root.val:
                rst.append(path[:])
        else:
            self.dfs(root.left,sum-root.val,rst,path)
            self.dfs(root.right,sum-root.val,rst,path)
        path.pop()
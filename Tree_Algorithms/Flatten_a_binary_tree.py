# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:31:49 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if(root==None):
            return None
        if(root.right == None and root.left == None):
            return root
        temp = root.right
        root.right=self.flatten(root.left)
        root.left=None
        p=root
        while(p.right):
            p=p.right
        p.right = self.flatten(temp)
        return root

class Solution2:
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
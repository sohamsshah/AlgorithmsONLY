# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:00:25 2020

@author: Soham Shah
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#recursive
class Solution:
    def helper(self,root: 'Node'):
        if root is None:
            return []
        tree = []
        for child in root.children:
            tree+=self.helper(child)
            tree+=[child.val]
        return tree
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = self.helper(root)
        return ans+[root.val]
    
#iterative
        
def postorder(self, root):
        res = []
        if root == None: return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]    
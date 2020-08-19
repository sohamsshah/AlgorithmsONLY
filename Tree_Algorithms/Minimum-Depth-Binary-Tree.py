# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:38:53 2020

@author: Soham Shah
"""

class Solution:

    def minDepth(self, root):
        if not root:
            return 0
        else:
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        depth = 99999999
        queue = [(root,1)]
        while queue:
            curr, d = queue.pop(0)
            if not curr.right and not curr.left:
                depth = min(depth,d)
            if curr.left:
                queue.append((curr.left, d+1))
            if curr.right:
                queue.append((curr.right,d+1))
        return depth
            

        
        
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:31:00 2020

@author: Soham Shah
"""

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        present = 0
        previous = "p"
        minimum = 100000000
        while True:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                if len(stack) == 0:
                    break
                root = stack.pop()
                
                if previous == "p":
                    previous = root.val
                else:
                    present = root.val
                    if minimum >= (present - previous):
                        minimum =  present - previous
                    previous = root.val
                
                    
                root = root.right
        return (minimum)


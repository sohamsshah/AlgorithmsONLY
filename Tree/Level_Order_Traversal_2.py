# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:44:56 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue1 = [root]
        queue2 = []
        traversal = []
        temp = []
        toggle = 1
        while True:
            if len(queue1) == 0 and len(queue2)==0:
                break
            if toggle == 1:
                while(queue1):
                    node = queue1.pop(0)
                    if node.left != None:
                        queue2.append(node.left)
                    if node.right != None:
                        queue2.append(node.right)
                    temp.append(node.val)   
                if temp != []:
                    traversal.append(temp)
                temp = []
                toggle = 2
            if toggle == 2:
                while(queue2):
                    node = queue2.pop(0)
                    if node.left != None:
                        queue1.append(node.left)
                    if node.right != None:
                        queue1.append(node.right)
                    temp.append(node.val)   
                if temp != []:
                    traversal.append(temp)
                temp = []
                toggle = 1
        return traversal[::-1]
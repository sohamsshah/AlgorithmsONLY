# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:58:25 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        traversal=[]
        queue = [root,-999999]
        temp =[]
        while(queue != [-999999]):
            node = queue.pop(0)
            if node==-999999:
                traversal.append(temp)
                temp = []
                queue.append(-999999)
            else:
                if node!= None:
                    temp.append(node.val)
                    if node.left != None:
                        queue.append(node.left)
                    if node.right != None:
                        queue.append(node.right)

        return (traversal+[temp])
            
            
                
            
                
        
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:29:22 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        arr = []
        root_values = self.level_order(root)
        height = len(root_values)
        indices = []
        for i in root_values:
            temp = []
            for j in i:
                temp+=([""]*(((2**height)-1)//2))
                temp+=([str(j)])
                temp+=([""]*(((2**height)-1)//2))
            for i in indices:
                temp.insert(i,"")
            indices = self.get_indices(temp)
            arr.append(temp.copy())
            height-=1
            
        return arr
    def get_indices(self,lis):
        ans = []
        for i in range(len(lis)):
            if lis[i] != "":
                ans.append(i)
        return ans
                
        
    def level_order(self,root):
        queue = [root,None]
        ans = [[root.val]]
        temp =[]
        while True:
            curr = queue.pop(0)
            if curr == "":
                break
            if curr == None:
                ans.append(temp.copy())
                temp = []
                queue.append(None)
            else:
                if curr.left:
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                if not curr.left:
                    queue.append("")
                    temp.append("")
                if not curr.right:
                    queue.append("")
                    temp.append("")
                if curr.right:
                    queue.append(curr.right)
                    temp.append(curr.right.val)
        for i in ans:
            if i.count("") == len(i):
                ans.remove(i)
                
        return ans
                    
                
            
                    
            
        
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:41:48 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: TreeNode) -> List[int]:
        dic = {}
        if root is None:
            return []
        def helper(node):
            if node == None:
                return
            if node.val not in dic:
                dic[node.val]=1
            else:
                dic[node.val]+=1
            helper(node.left)
            helper(node.right)
        helper(root)
        maxi = max(list(dic.values()))
        ans = []
        for i in dic:
            if dic[i] == maxi:
                ans.append(i)
        return ans
            
        
        
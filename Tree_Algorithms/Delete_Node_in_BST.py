# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:38:12 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def inorder_predecessor(root):
            root = root.left
            while root.right != None:
                root= root.right
            return root.val
        def inorder_successor(root):
            root = root.right
            while root.left != None:
                root= root.left
            return root.val
        
        if root is None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None and root.right == None:
                root = None
            elif root.left != None:
                root.val = inorder_predecessor(root)
                root.left = self.deleteNode(root.left,root.val)
            elif root.right != None:
                root.val = inorder_successor(root)
                root.right = self.deleteNode(root.right,root.val)
                        
        return root
        
        
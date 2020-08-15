# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:59:11 2020

@author: Soham Shah
"""
#tree traversal best method to save in arr
def traverse(root, arr):
            
    if root is None:
        return
    arr.append(root.val)
    traverse(root.left, arr)
    traverse(root.right,arr)
    return arr



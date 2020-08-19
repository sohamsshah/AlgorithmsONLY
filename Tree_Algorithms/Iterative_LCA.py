# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:45:59 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        temp = []
        if p == root or q == root:
            return root
        if root.right != None and root.left != None:
            dic = {root.right.val:[root.val], root.left.val:[root.val]}
        elif root.right == None and root.left != None:
            dic = {root.left.val:[root.val]}
        else:
            dic = {root.right.val:[root.val]}
            
            
        while True:
            if len(stack) == 0:
                break
            node = stack.pop()
            temp.append(node)
            if node.right != None:
                stack.append(node.right)
                if node != root:
                    dic[node.right.val] = dic[node.val] + [node.val]  
            if node.left != None:
                stack.append(node.left)
                if node != root:
                    dic[node.left.val] = dic[node.val] + [node.val] 
        
        dic[p.val].append(p.val)
        first = list(dic[p.val])
        dic[q.val].append(q.val)
        second = list(dic[q.val])
        for i,j in zip(first,second):
            if i != j:
                break
            ans = i
        for i in temp:
            if i.val == ans:
                return i
            
# Better Approach
                
class Solution2:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
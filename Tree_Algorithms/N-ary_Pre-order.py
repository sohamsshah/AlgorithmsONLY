# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:10:13 2020

@author: Soham Shah
"""

#recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        tree = [root.val]
        if root.children:
            for child in root.children:
                tree += self.preorder(child)
        return tree

#iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            ans.append(curr.val)
            temp = []
            for child in curr.children:
                if child is not None:
                    temp.append(child)   
            queue = temp+queue
        return ans
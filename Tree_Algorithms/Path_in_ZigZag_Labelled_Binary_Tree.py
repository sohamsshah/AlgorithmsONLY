# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:21:13 2020

@author: Soham Shah
"""

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        while label >= 1:
            ans.insert(0, label)
            label= label//2
        print(ans)   
        for i in range(1,len(ans)):
            if len(ans)%2 == 0:
                if i%2 == 0:
                    ans[i] = (2**(i+1)-1) - ans[i] + (2**(i)-1) + 1
            else:
                if i%2 != 0:
                    ans[i] = (2**(i+1)-1) - ans[i] + (2**(i)-1) + 1
                
        return (ans)
            
  